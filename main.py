import cv2
import numpy as np
import glob
import os
import re

CHESS_PIECE_DIR = glob.glob('chess_piece/*.*')
CHESS_BOARD_DIR = glob.glob('test/*.*')
CHESS_BOARD_OUTPUT_DIR = os.path.join('dist')

SHOW_IMAGE = True
EXPORT_IMAGE = True

chessPieceThreshold = {
    'bishop': 0.2,
    'bishop_black': 0.3,
    'king': 0.2,
    'king_black': 0.2,
    'knight':0.1,
    'knight_black': 0.2,
    'pawn': 0.15,
    'pawn_black': 0.3,
    'queen': 0.2,
    'queen_black': 0.2,
    'rook': 0.2,
    'rook_black': 0.2,
}

chessPieceImages = dict()

for path in CHESS_PIECE_DIR:
    baseName = os.path.basename(path)
    fileName = re.search('[\w() -]+?(?=\.)', baseName).group(0)
    pieceImage = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    chessPieceImages[fileName] = (pieceImage, chessPieceThreshold[fileName])
    
chessBoardImages = dict()

for idx, path in enumerate(CHESS_BOARD_DIR):
    baseName = os.path.basename(path)
    fileName = re.search('[\w() -]+?(?=\.)', baseName).group(0)
    boardImage = cv2.imread(path)
    chessBoardImages[fileName] = boardImage
    
    
def detectPieceOfChess(boardName, boardImage):
    for piece in chessPieceImages:
        pieceImage = chessPieceImages[piece][0]
        pieceThreshold = chessPieceImages[piece][1]
        pieceColor = 'black' if piece.find('black') > 0 else 'white'
        pieceName = piece
        
        boardImageGray = cv2.cvtColor(boardImage, cv2.COLOR_BGR2GRAY)
        pieceImageGray = cv2.cvtColor(pieceImage, cv2.COLOR_BGR2GRAY)
        
        mask = pieceImage[:,:,3]
        h, w = pieceImageGray.shape
            
        result = cv2.matchTemplate(boardImageGray, pieceImageGray, cv2.TM_SQDIFF_NORMED, mask=mask)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        while min_val < pieceThreshold:
            top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            
            rectangleColor = (0,250,50)
            cv2.rectangle(boardImage, top_left, bottom_right, rectangleColor, 2)
                          
            textColor = (200,20,20)
            textPosition =  (top_left[0], top_left[1] + 10) 
            cv2.putText(boardImage, pieceName[:3], textPosition, cv2.FONT_HERSHEY_SIMPLEX, 0.5, textColor, 1, cv2.LINE_AA)
            
            # overwrite the portion of the result that has the match:
            h1 = top_left[1]-h//2
            h1 = np.clip(h1, 0, result.shape[0])

            h2 = top_left[1] + h//2 + 1
            h2 = np.clip(h2, 0, result.shape[0])

            w1 = top_left[0] - w//2
            w1 = np.clip(w1, 0, result.shape[1])

            w2 = top_left[0] + w//2 + 1
            w2 = np.clip(w2, 0, result.shape[1])
            
            # poison the result in the vicinity of this match so it isn't found again
            result[h1:h2, w1:w2] = 1
            
            # look for next match
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
    if EXPORT_IMAGE:
        cv2.imwrite(os.path.join(CHESS_BOARD_OUTPUT_DIR, boardName + '.jpg'), boardImage)
        
    if SHOW_IMAGE:
        cv2.imshow(boardName, boardImage)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
for boardName in chessBoardImages:
    detectPieceOfChess(boardName, chessBoardImages[boardName])