import numpy as np 
import cv2

#~ img = cv2.imread('stapler.jpg')
cap = cv2.VideoCapture(0)
_,frame = cap.read()
retval, threshold = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
retval2, threshold2 =cv2.threshold(grayscaled, 100, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)
retval2, otsu = cv2.threshold(grayscaled, 125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("original", frame)
cv2.imshow("threshold",threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destoryAllWindows()  
