import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')

kernel = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
print(kernel)

dilation = cv.dilate(img,kernel,iterations = 1)
closing = cv.erode(dilation,kernel,iterations = 1)
plt.subplot(1, 2, 2),plt.imshow(closing, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title("output by erosion and dilation")

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
plt.subplot(1, 2, 2),plt.imshow(closing, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title("output by morphologyEX function")
plt.show()