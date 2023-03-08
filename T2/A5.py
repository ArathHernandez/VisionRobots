import cv2 as cv
import numpy as np

imagen = np.zeros([400,400], dtype=np.uint8)
nms = np.linspace(255,0,400).astype(np.uint8)
for i in range (400):
    imagen[:,i] = nms    

cv.imshow("Gradiente", imagen)
cv.waitKey()
