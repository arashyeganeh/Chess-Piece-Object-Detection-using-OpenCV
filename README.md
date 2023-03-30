# Chess Piece Detection | OpenCV `matchTemplate()`

<p>
	<img alt="python" src="https://img.shields.io/badge/Python-1E90FF?logo=python&logoColor=white">
    <img alt="opencv" src="https://img.shields.io/badge/OpenCV-1F3AF7?logo=opencv&logoColor=01F701">
    <img alt="numpy" src="https://img.shields.io/badge/OpenCV-4AA6C9?logo=numpy&logoColor=white">
    <img alt="jupyter" src="https://img.shields.io/badge/Jupyter-ededed?logo=jupyter&logoColor=F37726"/>
</p>

This project involves loading multiple images of chess boards and utilizing the matchTemplate method of OpenCV to detect the pieces present on each board. As a result of this process, the output includes a comprehensive list of the detected chess piece names.

<p align="center">
    <img src="dist/board.jpg" />
    <img src="dist/board (9).jpg" />
    <img src="dist/board (10).jpg" />
    <img src="dist/board (1).jpg" />
</p>

## Requirements

- Python 3.x
- OpenCV
- Numpy

## Usage

To get started, first clone the repository and install the necessary dependencies by running the following command:

```bash
pip install opencv-python numpy
```

Next, place the chess board image files in the `test/` directory and the chess piece image files in the `chess_piece/` directory.

There are two ways to execute the program:

**Method 1: Running in Terminal**

To run the script in the terminal, use the following command:

```bash
python main.py
```

**Method 2: Running in Jupyter Lab**

To run the script in `Jupyter Lab`, open the `main.ipynb` notebook and execute the code.

## Configuration

The following configurations can be adjusted according to the user's preference:

- `SHOW_IMAGE`: If set to `True`, the image with detected pieces will be displayed. Default is `True`.
- `EXPORT_IMAGE`: If set to `True`, the image with detected pieces will be saved to the `dist/` directory. Default is `True`.
- `chessPieceThreshold`: The threshold values for each chess piece can be adjusted according to the image quality. The default values are provided in the script.
- `CHESS_BOARD_OUTPUT_DIR`: The directory where the output images will be saved. Default is `dist/`.

## License

This project is licensed under the MIT License.
