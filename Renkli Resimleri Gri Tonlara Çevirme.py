import cv2

image = cv2.imread("foto.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('Gri Foto.jpg', gray_image)

cv2.imshow('Gri foto', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
