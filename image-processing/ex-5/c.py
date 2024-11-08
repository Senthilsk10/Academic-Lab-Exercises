import numpy as np
import pywt
from matplotlib import pyplot as plt


import cv2

img = cv2.imread('download.jpeg',0)

coeffs = pywt.dwt2(img,'bior1.3')
#print(coeffs)
ca,(ch,cv,cd) = coeffs

plt.subplot(121)
plt.imshow(ca,cmap='gray')
plt.title("aproximation co efficient")
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(ch,cmap='gray')
plt.title("horizontal co efficient")
plt.xticks([])
plt.yticks([])
plt.show()
reconst = pywt.idwt2(coeffs,'bior1.3')

plt.imshow(reconst,cmap='gray')
plt.title('reconstructed')


plt.xticks([])

plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
