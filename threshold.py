import cv2 

img = cv2.imread('lena.jpeg')
# 二值化阈值处理
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#反二值化阈值处理
ret2,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#截断阈值化处理  
ret3,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)


cv2.imshow('img',img)
cv2.imshow('thresh1',thresh1)
cv2.imshow('thresh2',thresh2)
cv2.imshow('thresh3',thresh3)

cv2.waitKey()
cv2.destroyAllWindows()