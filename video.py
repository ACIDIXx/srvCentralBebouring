#!/usr/bin/env python
# use python 2.7 / prerequis : numpy et open cv 2.4.x pour cv2.pyd (x86)
import cv2


cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
i = 0
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
	cv2.imshow("preview", frame)
	rval, frame = vc.read()
	cv2.imwrite("C:/Users/Acidix/Desktop/jjh/frame.jpg", frame)
	
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
cv2.destroyWindow("preview")