import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/DELL/Downloads/image.png", cv2.IMREAD_UNCHANGED)

# Check if the image has an alpha channel
if image.shape[2] == 4:
    # Image already has an alpha channel, separate it
    bgr_image = image[:, :, :3]
    alpha_image = image[:, :, 3]
else:
    # Image does not have an alpha channel, create one
    bgr_image = image
    alpha_image = np.ones((bgr_image.shape[0], bgr_image.shape[1]), dtype=np.uint8) * 255

# Convert the image to grayscale
gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

# Create a mask where pixel values less than 30 are True
mask = gray < 30

# Create an output image with an alpha channel
output = np.zeros((bgr_image.shape[0], bgr_image.shape[1], 4), dtype=np.uint8)

# Copy the BGR channels to the output image
output[:, :, :3] = bgr_image

# Set the alpha channel: 255 for pixels less than 30, 0 for others
output[:, :, 3] = np.where(mask, 255, 0)

# Save the result
cv2.imwrite('output_image.png', output)

# Optionally, display the result
# cv2.imshow('Result', output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
