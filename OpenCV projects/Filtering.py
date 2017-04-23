import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv hue(type of colour) sat(eg how red it is) value(how bright it is)
	lower_blue = np.array([70,70,50])
	upper_blue = np.array([130,180,255])
	
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	median = cv2. medianBlur(res, 15)
	
	
	cv2.imshow("frame", frame)
	#~ cv2.imshow("mask", mask)
	#~ cv2.imshow("res", res)
	cv2.imshow("median", median)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2. destoryAllWindows()
cap.release() 
