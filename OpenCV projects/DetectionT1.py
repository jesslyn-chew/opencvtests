import cv2
import numpy as np

image = cv2.imread("green.jpg")

#Filter to only green circle
while True:
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#hsv hue(type of colour) sat(eg how red it is) value(how bright it is)
	lower_green = np.array([0,0,0])
	upper_green = np.array([255,255,255])
	
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(image,image,mask = mask)
	
	output = image.copy()
	cimg = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)	
	
	# detect circles in the image
	# cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, max Radius[)
	circles = cv2.HoughCircles(cimg, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 10, param1=30,param2=50)

	#convert the (x,y) coordinate and radius of the circle to integers
	circles = np.uint16(np.around(circles[0, :]))

	# ensure atleast some circles were found 
	if circles is not None:
	
		#loop 
		for (x, y, r) in circles:
			#draw the outline of circle and a rectangle to pinpoint the center
			cv2.circle(output, (x,y) , r, (0,0,0),4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0,128,255), -1)
		
		# show output image
		cv2.imshow("output", np.hstack([image,output]))
		cv2.waitKey(0)
	cv2. destoryAllWindows()

#Detection for circles is decent, but in terms of color it has some problems
