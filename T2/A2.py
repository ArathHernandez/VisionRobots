import cv2 as cv
import numpy as np

row = 400
col = 400

imagen = np.zeros([row,col,3], dtype=np.uint8)
for i in range (0, row, 100):
    for j in range (0, col, 100):
        imagen[i:i+49,j:j+49] = 255
        imagen[i+49:i+(2*49), j+49:j+(2*49)] = 255
cv.imshow('Chessboard', imagen)
cv.waitKey()
