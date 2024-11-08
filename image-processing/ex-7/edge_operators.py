import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cropped_image.jpg', cv2.IMREAD_GRAYSCALE)
img_gaussian = cv2.GaussianBlur(img,(3,3),0)

img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


plt.figure(figsize=(10, 7))
plt.subplot(3, 3, 2), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
cmap='gray'), plt.xticks([]), plt.yticks([]) ,plt.title('Original Image')
plt.subplot(3, 3, 4), plt.imshow(img_sobelx, cmap='gray'),plt.xticks([]),
plt.yticks([]), plt.title('Sobel X')
plt.subplot(3, 3, 5), plt.imshow(img_sobely, cmap='gray'), plt.xticks([]),
plt.yticks([]), plt.title('Sobel Y')
plt.subplot(3, 3, 6), plt.imshow(img_sobel, cmap='gray'),plt.xticks([]),
plt.yticks([]), plt.title('Sobel Edges')
plt.subplot(3, 3, 7), plt.imshow(img_prewittx, cmap='gray'),plt.xticks([]),
plt.yticks([]), plt.title('Prewitt X')
plt.subplot(3, 3, 8), plt.imshow(img_prewitty, cmap='gray'),plt.xticks([]),
plt.yticks([]), plt.title('Prewitt Y')
plt.subplot(3, 3, 9), plt.imshow(img_prewittx + img_prewitty,
cmap='gray'),plt.xticks([]), plt.yticks([]), plt.title('Prewitt Edges')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()