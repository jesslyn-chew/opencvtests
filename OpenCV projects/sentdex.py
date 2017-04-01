import cv2
import numpy as np

# def webcam, can also load a videofile by changing 0 to eg "Video.avi"
cap = cv2.VideoCapture (0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# while true to crate an infinite loop, ret(T/F) 
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
#out.release()
cv2.destoryAllWindows() 
	
