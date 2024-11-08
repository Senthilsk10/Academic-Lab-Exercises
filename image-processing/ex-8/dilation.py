import cv2 as cv
import matplotlib.pyplot as plt
# Load and display the input image
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
print(kernel)
dilation = cv.dilate(img,kernel,iterations = 1)

plt.subplot(1, 2, 2),plt.imshow(dilation, cmap='gray')
plt.title("output image")
plt.xticks([]), plt.yticks([])
plt.show()