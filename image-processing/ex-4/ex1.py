import cv2 

img = cv2.imread("download.jpeg")
k= (3,3)

blured = cv2.blur(img,k)

cv2.imshow('blured',blured)
cv2.waitKey(0)
cv2.destroyAllWindows()
