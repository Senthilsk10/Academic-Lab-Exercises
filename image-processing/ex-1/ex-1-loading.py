import cv2

img = cv2.imread("photo_2023-11-11_16-33-25.jpg")
cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()