import cv2 

img = cv2.imread('lena.jpeg')
#均值滤波
r = cv2.blur(img,(5,5))
r2 = cv2.blur(img,(20,20))
#方框滤波
r3 = cv2.boxFilter(img,-1,(5,5) ,normalize=1)
#高斯滤波
r4 = cv2.GaussianBlur(img,(7,7),0,0)
#中值滤波
r5 = cv2.medianBlur(img,3)
#双边滤波
r6 = cv2.bilateralFilter(img,25,100,100)

cv2.imshow('result',r)
cv2.imshow('result2',r2)
cv2.imshow('result3',r3)
cv2.imshow('result4',r4)
cv2.imshow('result5',r5)
cv2.imshow('result6',r6)

cv2.waitKey()
cv2.destroyAllWindows()