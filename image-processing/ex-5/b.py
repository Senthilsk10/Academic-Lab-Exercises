import numpy as np

import cv2

img = cv2.imread('download.jpeg',0)

img = np.float32(img)

dct = cv2.dct(img,cv2.DCT_INVERSE)
img1  = cv2.idct(dct)
img1 = np.uint8(img1)

cv2.imshow("dct image",dct)
cv2.imshow("inversed image",img1)# both ways the file size was increased , then how come it was used for compression
#cv2.imwrite('inversed1.jpg',dct)
cv2.waitKey(0)
cv2.destroyAllWindows()
