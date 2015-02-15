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
	return getText(img, (x1, y1), (x2,y2))

#place img2 onto img1 at loc p1.x, p1.y
def compImage(img1, img2, p1, p2):
	img1[p2[0] + (p2[1]//4):p2[1], p1[0]:p1[1] - (p1[1]//3)]= img2
	return img1

def getText(img, p1, p2):
	crop_img = img[p2[0] + (p2[1]//4):p2[1], p1[0]:p1[1] - (p1[1]//3)]
	bkup = crop_img.copy()
	hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

	#rgb 97 150 187
	# define range of blue color in HSV
	#Perfect 204, 48, 73

	#blue = ([86, 31, 4], [220, 88, 50])
	#blue = ([171,40,48], [220, 60, 80])
	crop_img = cv2.blur(crop_img, (1,1))
	#blue = ([100, 100, 75], [230, 230, 230])
	blue = ([175, 145, 85], [200, 170, 110])

	lower_col = np.array(blue[0], dtype=np.uint8)
	upper_col = np.array(blue[1], dtype=np.uint8)

	mask = cv2.inRange(crop_img, lower_col, upper_col)
	res = cv2.bitwise_and(crop_img,crop_img, mask= mask)
	vis = np.concatenate((bkup, crop_img), axis=0)
	vis = np.concatenate((vis, res), axis=0)

	return vis #compImage(img, res, p1, p2)

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

	#frameset = 1000#1040
   	#vidFile.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frameset)

	ret, frame = vidFile.read() # read first frame, and the return code of the function.

	while ret:  # note that we don't have to use frame number here, we could read from a live written file.
		cv2.imshow("frameWindow", getROI(frame))
		cv2.waitKey(int(1/fps*1000)) # time to wait between frames, in mSec
		ret, frame = vidFile.read() # read next frame, get next return code
		timestmp = vidFile.get(cv2.cv.CV_CAP_PROP_POS_MSEC) / 1000
		framestmp = vidFile.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
		print("{0:.2f} seconds "+str(int(framestmp))+" frames \r").format(timestmp),
		sys.stdout.flush()





