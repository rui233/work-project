import cv2

img = cv2.imread('lena.jpeg',0)
cv2.namedWindow('lenna',cv2.WINDOW_NORMAL)
cv2.imshow('lenna',img)
cv2.waitKey(0)
cv2.imwrite('lenna_gray.jpg',img)