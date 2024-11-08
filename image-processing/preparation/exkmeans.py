import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('..\download.jpeg')

pix_val = cv.cvtColor(img,cv.COLOR_BGR2RGB)
pix_val = pix_val.reshape((-1,3))
pix_val = np.float32(pix_val)

criteria = (cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,100,0.85)
ret,label,centers = cv.kmeans(pix_val,2,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
segmented = centers[label.flatten()]
segmented = segmented.reshape((img.shape))
plt.imshow(segmented)
plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()