import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	
	#~ Change the color type from BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#~ hsv hue(type of colour) sat(eg how red it is) value(how bright it is)
	lower_green = np.array([45,50,0])
	upper_green = np.array([70,255,200])
	mask = cv2.inRange(hsv, lower_green, upper_green)
	
	#~ Filtering
	res = cv2.bitwise_and(frame, frame, mask = mask)
	median = cv2. medianBlur(res, 15)
	imgray = cv2.cvtColor(median,cv2.COLOR_BGR2GRAY)
	
	bilateral_filtered_image = cv2.bilateralFilter(imgray, 5, 175, 175)
	edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
	contours, hierarchy = cv2.findContours(edge_detected_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	contour_list= []
	for contour in contours:
		approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour,True),True)
		area= cv2.contourArea(contour)
		if ((len(approx) > 10) & (len(approx) < 15) & (area>50) ):
			contour_list.append(contour)
			
			M = cv2.moments(contour)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			print (cx, cy)
			img = cv2.circle(frame,(cx,cy), 3, (0,0,255), -1)
			
	cv2.drawContours(frame, contour_list, -1, (0,255,0), 3)
	
	cv2.imshow("x", median)
	cv2.imshow("frame", frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2. destroyAllWindows()
cap.release()
