import cv2
import numpy as np

img = cv2.imread('./logo.jpg',0)
minmax_img = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')

"""
s = set()
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        s.add(img[i,j])
print(s)
for e  in s:
    print(((e-0)/255-0)*255)
"""
cv2.imshow('previous image',minmax_img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        minmax_img[i,j] = (img[i,j]-np.min(img))/(np.max(img)-np.min(img))*255
        #print(minmax_img[i,j])

cv2.imshow('Original Image',img)
cv2.imshow('Contrast Stretched',minmax_img)
cv2.waitKey(0)
cv2.destroyAllWindows()