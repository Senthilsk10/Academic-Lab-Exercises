import cv2
import numpy as np

image1 = cv2.imread('./download.jpeg', cv2.COLOR_BGR2GRAY)
image = cv2.imread('./download.jpeg', cv2.IMREAD_GRAYSCALE)

image_float = np.float32(image)

c = 255 / np.log(1 + np.max(image_float))
log_image = c * (np.log(1 + image_float))

log_image = np.uint8(log_image)

cv2.imshow('Original Color Image', image1)
cv2.imshow('Gray Scaled Image', image)
cv2.imshow('Log Transformed Image', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()