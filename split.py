import cv2 

img = cv2.imread('lena.jpeg')
'''
b,g,r = cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.waitKey(0)
'''
# or using index in numpy

b = img[:,:,0]
cv2.imshow('blue',b)
cv2.waitKey(0)

