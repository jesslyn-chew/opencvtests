import cv2
import numpy as np 

while True:
	img = cv2.imread('plane.png')
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_purple = np.array([140,100,0])
	upper_purple = np.array([170,255,255])
	mask = cv2.inRange(hsv, lower_purple , upper_purple) 
	
	res = cv2.bitwise_and(img, img, mask = mask)
	imgray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
		
	bilateral_filtered_image = cv2.bilateralFilter(imgray, 5, 175, 175)
	edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
	contours, hierarchy = cv2.findContours(edge_detected_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contour_list = []

	h = hierarchy[0]
	for component in zip(contours,h):
		currentcontour = component[0]
		currenthierarchy = component[1]
		approx = cv2.approxPolyDP(currentcontour, 0.01* cv2.arcLength(currentcontour,True),True)
		area= cv2.contourArea(currentcontour)	
		if currenthierarchy[3] > 0 and currenthierarchy[2] < 0 and (len(approx) >5):	
			contour_list.append(currentcontour)
			
			M = cv2.moments(currentcontour)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			print (cx, cy)
			cv2.circle(img,(cx,cy), 3, (255,0,0), -1)
			
	C = cv2.drawContours(img, contour_list, -1, (0,0,255), 2)	
	
	cv2.imshow("res", res)
	cv2.imshow("frame", img)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2. destroyAllWindows()

