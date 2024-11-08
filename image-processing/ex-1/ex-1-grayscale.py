import cv2
img = cv2.imread("photo_2023-11-11_16-33-25.jpg")

cv2.imshow("original image" , img)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscaled image" , grayscaled)

cv2.waitKey(0)
cv2.destroyAllWindows()