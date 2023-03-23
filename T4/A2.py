import cv2

imagen = cv2.imread('Perrillos.jpg', cv2.IMREAD_GRAYSCALE)
imagen = cv2.resize(imagen, (400,400))

sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1)
laplacian = cv2.Laplacian(imagen, cv2.CV_64F)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow('Sobel en X', sobel_x)
cv2.imshow('Sobel en Y', sobel_y)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
