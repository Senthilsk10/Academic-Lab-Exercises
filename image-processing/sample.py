import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "C:/Users/DELL/Downloads/crater example.jpeg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection using the Canny edge detector
edges = cv2.Canny(gray, 100, 200)

# Find contours from the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty image to draw the contours on
contour_image = np.zeros_like(image)

# Draw the contours on the empty image
cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 1)

# Display the original image and the image with contours
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Contours Image')
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))

plt.show()

# Extract and print the coordinates of the contours
for i, contour in enumerate(contours):
    print(f"Contour #{i + 1}:")
    for point in contour:
        print(f"({point[0][0]}, {point[0][1]})")
