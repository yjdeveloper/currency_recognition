"""
Project: How to automatically crop the digit using OpenCV
Author: Yonten Jamtsho
Date Created: September 3, 2021
Description: This project will automatocally crop the object in the image based on the area
# of the contours 
"""

# import libraries
import cv2 as cv
from time import time
import argparse as ap
from time import time

Folder_name = "Cropped/"

# Construct the argument parser
arg = ap.ArgumentParser()
arg.add_argument('-i', '--image', required = True, help="Path to the image")
args = vars(arg.parse_args())

# Read the image
img = cv.imread(args['image'])

# Convert the grayscale image to binary
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 230), we set it to be *black, otherwise it is *white*
ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

# Find the contours on the thresholded binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Draw a bounding box around the first contour
# x is the starting x coordinate of the bounding box
# y is the starting y coordinate of the bounding box
# w is the width of the bounding box
# h is the height of the bounding box
for c in contours:
	t = time()
	area = cv.contourArea(c)
	# Filter out unwanted contours
	if area > 10000:
		# print(area)
		(x, y, w, h) = cv.boundingRect(c)
		if x > 50 and y > 50 and w > 50 and h > 50:
			# Here, 50 is added/subtracted so that we have a some space between object and edge of the image
			startX = x - 50
			startY = y - 50
			endX = x + w + 50
			endY = y + h + 50

			crop_img = img[startY:endY, startX:endX]

			# cv.rectangle(img,(x - 50, y - 50), (x + w + 50, y + h + 50), (255, 255, 255), 1)
			# cv.namedWindow("Image", cv.WINDOW_NORMAL)
			# cv.imshow('Image', img)
			cv.imwrite(Folder_name + str(t) + ".jpg", crop_img)
			# cv.waitKey(0)