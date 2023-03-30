# Chess Piece Detection

This project demonstrates the detection of chess pieces on a chess board using OpenCV.

## Requirements

- Python 3.x
- OpenCV
- Numpy

## Usage

1. Clone the repository.
2. Install the required dependencies using the following command:

```
Copy code
pip install -r requirements.txt
```

1. Put the chess board image files under `test/` directory and chess piece image files under `chess_piece/` directory.
2. Run the script using the following command:

```
Copy code
python chess_piece_detection.py
```

## Configuration

The following configurations can be adjusted according to the user's preference:

- `SHOW_IMAGE`: If set to `True`, the image with detected pieces will be displayed. Default is `True`.
- `EXPORT_IMAGE`: If set to `True`, the image with detected pieces will be saved to the `dist/` directory. Default is `True`.
- `chessPieceThreshold`: The threshold values for each chess piece can be adjusted according to the image quality. The default values are provided in the script.
- `CHESS_BOARD_OUTPUT_DIR`: The directory where the output images will be saved. Default is `dist/`.

## License

This project is licensed under the MIT License.
