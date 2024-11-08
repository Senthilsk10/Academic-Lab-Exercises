import cv2 
import numpy as np
img = cv2.imread("download.jpeg")

cv2.imshow("org",img)
filter_9 = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
]
    )
filter_8 = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
]
    )

sharpened = cv2.filter2D(img,-1,filter_9)
cv2.imshow("9",sharpened)
sharpened8 = cv2.filter2D(img,-1,filter_8)
cv2.imshow("8",sharpened8)

cv2.waitKey(0)
cv2.destroyAllWindows()
