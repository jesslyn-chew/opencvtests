import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv hue(type of colour) sat(eg how red it is) value(how bright it is)
	lower_purple = np.array([50,0,0])
	upper_purple = np.array([70,255,255])
	
	mask = cv2.inRange(hsv, lower_purple, upper_purple)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	median = cv2. medianBlur(res, 15)
	
	output = frame.copy()
	cimg = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)	
	
	# detect circles in the image
	# cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, max Radius[)
	circles = cv2.HoughCircles(cimg, cv2.cv.CV_HOUGH_GRADIENT, 2, 10, param1=30,param2=50, minRadius=0, maxRadius=100)

		# ensure atleast some circles were found 
	if circles is not None:
		#convert the (x,y) coordinate and radius of the circle to integers
		circles = np.uint16(np.around(circles[0, :]))

		#loop 
		for (x, y, r) in circles:
			#draw the outline of circle and a rectangle to pinpoint the center
			cv2.circle(output, (x,y) , r, (0,0,0),4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0,128,255), -1)
			print(x,y)
		
	# show output image
	cv2.imshow("output", output)
	#cv2.imshow("frame", frame)
	#cv2.imshow("mask", mask)
	#cv2.imshow("res", res)
	cv2.imshow("median", median)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2. destoryAllWindows()
cap.release() 
