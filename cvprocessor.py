import cv2


"""Returns true if every pixel in the image is not black"""
def hasNoBlack(frame):
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	return cv2.countNonZero(gray) == gray.size
