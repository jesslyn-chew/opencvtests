import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	#Change the color type from BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv hue(type of colour) sat(eg how red it is) value(how bright it is)
	lower_purple = np.array([50,0,0])
	upper_purple = np.array([70,255,255])
	
	#Filtering 
	mask = cv2.inRange(hsv, lower_purple, upper_purple)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	median = cv2. medianBlur(res, 15)
	
	
	bilateral_filtered_image = cv2.bilateralFilter(median, 5, 175, 175)
	edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)

	
	#changing to gray
	#~ gray = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)		
	#threshold not necessary?
	#~ ret, threshold = cv2.threshold(edge_detected_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#finding the contours
	contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#drawing contours

	contour_list = []
	for contour in contours:
		approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
		area = cv2.contourArea(contour)
		if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
			contour_list.append(contour)

			cv2.drawContours(frame,contours,-1,(0,0,255),6)

		
	# show output image
	cv2.imshow("frame", frame)
	#cv2.imshow("mask", mask)
	#cv2.imshow("res", res)
	#cv2.imshow("median", median)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2. destoryAllWindows()
cap.release() 
