#This should handle getting the text where your kills are. 
import cv
import cv2
import sys
import numpy as np

def getROI(img):
	height, width, depth = img.shape
	x1 = 0
	x2 = (int)(width//4)
	y1 = (int)(height//2 + height//6)
	y2 = (int)(3* height//4 + height//11)
	cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
	getText(img, (x1, y1), (x2,y2))
	return img

#place img2 onto img1 at loc p1.x, p1.y
def compImage(img1, img2, p1):
	img1[p1[0]:p1[0]+img2.shape[0], p1[1]:p1[1]+img2.shape[1]] = img2
	return img1

def getText(img, p1, p2):
	crop_img = img[p1[0]:p1[1], p2[0]:p2[1]]

	gray = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	samples =  np.empty((0,100))
	responses = []
	keys = [i for i in range(48,58)]

	for cnt in contours:
		if cv2.contourArea(cnt)>50:
			[x,y,w,h] = cv2.boundingRect(cnt)

			if  h>28:
				cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),2)
				roi = thresh[y:y+h,x:x+w]
				roismall = cv2.resize(roi,(10,10))

	return compImage(img, crop_img, p1)

def openVideoFile(fileToOpen):
	try:
		vidFile = cv2.VideoCapture(fileToOpen)
	except:
		print "problem opening input stream"
		sys.exit(1)
	if not vidFile.isOpened():
		print "capture stream not open"
		sys.exit(1)
	nFrames = int(vidFile.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)) # one good way of namespacing legacy openCV: cv2.cv.*
	print "frame number: %s" %nFrames
	fps = vidFile.get(cv2.cv.CV_CAP_PROP_FPS)
	print "FPS value: %s" %fps

	ret, frame = vidFile.read() # read first frame, and the return code of the function.
	while ret:  # note that we don't have to use frame number here, we could read from a live written file.
		cv2.imshow("frameWindow", getROI(frame))
		cv2.waitKey(int(1/fps*1000)) # time to wait between frames, in mSec
		ret, frame = vidFile.read() # read next frame, get next return code