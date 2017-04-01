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
	ret, threshold = cv2.threshold(cimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	contours, hierarchy = cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	
	cv2.drawContours(image,contours,-1,(0,0,255),6)
 


	cv2.imshow("output", image)
	cv2.waitKey(0)
	cv2. destoryAllWindows()

#Detection for circles is decent, but in terms of color it has some problems
