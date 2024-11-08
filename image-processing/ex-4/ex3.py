import cv2 

img = cv2.imread("download.jpeg")

restored = cv2.medianBlur(img,3)
cv2.imwrite("restored_md_filter_k3.jpeg",restored)
cv2.waitKey(0)
cv2.destroyAllWindows()
