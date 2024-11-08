import cv2

image = cv2.imread('./sign.png')

print(image.dtype)# intensity finder 'k' if its 8 then 2^8 then intensity L = 2^8 (256)
img_neg = 255 - image #(L-1)- r->256 for white pixel , r->0 for black pixel for gray r->128


cv2.imshow('Input Image', image)
cv2.imshow('Negative', img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()