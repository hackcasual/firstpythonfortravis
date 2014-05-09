import cv2

def isWhiteImage(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	return cv2.countNonZero(gray) == gray.size
