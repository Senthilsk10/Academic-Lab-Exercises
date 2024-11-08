import cv2
import matplotlib.pyplot as plt

img = cv2.imread('logo.jpg', cv2.IMREAD_GRAYSCALE)

plt.hist(img.ravel(),256,[0,256]);

cv2.imshow('Input image', img)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Histogram using Matplotlib')
plt.show()

histr = cv2.calcHist([img],[0],None,[256],[0,256])

p1=plt.plot(histr)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Histogram using OpenCV')
plt.show()

cv2.normalize(histr, histr, 0, 1, cv2.NORM_MINMAX)
plt.plot(histr)
plt.xlabel('Gray Levels')
plt.ylabel('No. of Pixels')
plt.title('Normalized Histogram using OpenCV')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()