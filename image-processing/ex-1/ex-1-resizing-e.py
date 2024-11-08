import cv2
img = cv2.imread("logo.jpg",cv2.IMREAD_UNCHANGED)

cv2.imshow("original image" , img)


scale_percent = 40

w = 400
h = img.shape[1]
dim = (w,h)

resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

#ex-1-resizing-b.py
cv2.imshow("resized imge", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()