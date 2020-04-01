import cv2 

img = cv2.imread('lena.jpeg')
print(img.dtype)
print(img.size)
face = img[10:160,40:160]
cv2.imshow('face',face)
cv2.waitKey(0)