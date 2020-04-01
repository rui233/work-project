import cv2 

img = cv2.imread('lena.jpeg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('lena_gray',img_gray)
cv2.waitKey(0)
'''
# show all flags  
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
'''
