import cv2 as cv
import matplotlib.pyplot as plt
# Load and display the input image
img = cv.imread('restored.jpeg', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')

kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
print(kernel)

erosion = cv.erode(img,kernel,iterations = 1)
opening = cv.dilate(erosion,kernel,iterations = 1)

plt.subplot(1, 2, 2),plt.imshow(opening, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Opened Image')
plt.show()