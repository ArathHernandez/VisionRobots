import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)
imagen = cv2.resize(imagen, (800, 800))

cv2.imshow('Imagen B/N', imagen)

hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])

plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
