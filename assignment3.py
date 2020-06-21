import numpy as np
import cv2

cs = int(input("Enter canvas size in pixel ( multiple of 8 ): "))
c = int(n/8)
print(c)

checkerboard = np.zeros([cs,cs],dtype = 'uint8')
a = c
k = c* 2

for j in range(a,cs,k):
        for i in range(a,cs,k):
                checkerboard[j-a:j,i-a:i] = 255
                checkerboard[j:j+a,i:i+a] = 255
        
cv2.imshow('Checkboard 8*8',checkerboard)
cv2.waitKey(0)
cv2.destroyAllWindows()
