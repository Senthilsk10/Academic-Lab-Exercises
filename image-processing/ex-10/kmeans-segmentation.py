import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('butterfly.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixels = image.reshape(-1, 3).astype(np.float32)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
k = int(input("Enter the number of clusters: "))

_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

segmented_image = centers[labels.flatten()].reshape(image.shape).astype(np.uint8)

plt.imshow(segmented_image)
plt.axis('off')  
plt.show()
