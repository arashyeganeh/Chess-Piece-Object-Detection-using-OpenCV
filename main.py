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

# The threshold values for each chess piece can be adjusted according to the image quality
chessPieceThreshold = {
    'B': 0.2, #bishop
    'b': 0.3, #bishop_black
    'K': 0.2, #king
    'k': 0.2, #king_black
    'N': 0.1, #knight
    'n': 0.2, #knight_black
    'P': 0.15,#pawn
    'p': 0.3, #pawn_black
    'Q': 0.2, #queen
    'q': 0.2, #queen_black
    'R': 0.2, #rook
    'r': 0.2, #rook_black
}

chessPieceImages = dict()

for path in CHESS_PIECE_DIR:
    baseName = os.path.basename(path)
    fileName = re.search('[\w() -]+?(?=\.)', baseName).group(0)[0]
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
                          
            textColor = (255,0,0) if pieceName.isupper() else (0,0,255) # white piece is blue and black piece is red
            textPosition =  (top_left[0], top_left[1] + 20)
            cv2.putText(boardImage, pieceName, textPosition, cv2.FONT_HERSHEY_SIMPLEX, 0.7, textColor, 2, cv2.LINE_AA)
            
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
        
for boardName in chessBoardImages:
    detectPieceOfChess(boardName, chessBoardImages[boardName])
    
cv2.waitKey(0)
cv2.destroyAllWindows()