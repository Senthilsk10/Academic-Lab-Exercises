import cv2 as cv
import matplotlib.pyplot as plt
# Load and display the input image
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
plt.subplot(1, 2, 1),plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Input Image')
# Create a rectangular structuring element (kernel) of size 5×5
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
print(kernel)
# Erode the input image with the structuring element
erosion = cv.erode(img,kernel,iterations = 1)
# Display the eroded image
plt.subplot(1, 2, 2),plt.imshow(erosion, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Eroded Image')
plt.show()