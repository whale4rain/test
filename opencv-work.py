import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread("jihe.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,205,255,cv2.THRESH_BINARY)
contours,he=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
ret=cv2.drawContours(img,contours,-1,(0,255,0),8)
for i in range(len(contours)):
    epsilon=0.01*cv2.arcLength(contours[i],True)
    approx=cv2.approxPolyDP(contours[i],epsilon,True)
    corners=len(approx)
    if corners >=  10:
       a=i 
ret1=cv2.drawContours(img,contours[a],-1,(0,0,255),20)
cv_show('first',ret1)