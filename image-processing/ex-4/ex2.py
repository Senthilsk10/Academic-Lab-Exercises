import cv2 
import numpy as np
img = cv2.imread("s&p.jpeg",0)



m,n= img.shape
rst = np.zeros([m,n])

for i in range(1,m-1):
    for j in range(1,n-1):
        temp = [
            img[i,j+1],
            img[i,j-1],
            img[i,j],
            img[i+1,j],
            img[i+1,j-1],
            img[i-1,j-1],
            img[i-1,j+1],
            img[i-1,j]
        ]
        
        temp = sorted(temp)
        #print(temp)
        rst[i,j] = temp[4]
        #print(temp)
        
rst = rst.astype('uint8')
cv2.imshow("restored",rst)
cv2.imwrite('restored.jpeg',rst)


cv2.waitKey(0)
cv2.destroyAllWindows()
