import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('Numeros_Binarizacion.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Imagen en blanco y negro', imagen)

hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])

plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
