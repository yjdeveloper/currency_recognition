"""
Project: How to remove small blobs using OpenCV
Author: Yonten Jamtsho
Date Created: September 4, 2021
Description: This project will remove the small while blobs from the binary image
"""

import numpy as np
import cv2 as cv
import imutils
import glob
import os
import progressbar
from natsort import natsorted
# import pandas as pd

#### Test for individual digit

# # Construct the argument parser
# arg = ap.ArgumentParser()
# arg.add_argument('-i', '--image', required = True, help="Path to the image")
# args = vars(arg.parse_args())

# img = cv.imread(args['image'])
# # cv.namedWindow("[Img]", cv.WINDOW_NORMAL)
# # cv.imshow("[Img]", img)
# # cv.waitKey(0)

# # Convert the image into grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(gray.shape)

# # apply basic thresholding -- the first parameter is the image
# # we want to threshold, the second value is is our threshold
# # check; if a pixel value is greater than our threshold (in this
# # case, 230), we set it to be *black, otherwise it is *white*
# ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

# cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key=cv.contourArea, reverse=True)

# for c in cnts:
# 	cnt_area = cv.contourArea(c)
# 	if cnt_area <=  200:
# 		print(cnt_area)
# 		(x, y, w, h) = cv.boundingRect(c)
# 		thresh[y:y + h, x:x + w] = 0
# 		# cv.rectangle(thresh, (x, y), (x + w, y + h), (0, 0, 255), 1)

# cv.namedWindow("[Img]", cv.WINDOW_NORMAL)
# cv.imshow("[Img]", thresh)
# cv.waitKey(0)

##########################################

##### Test in bulk #####

# Path that will have the output
Folder_name = "Final/"

filenames = [img for img in glob.glob("Cropped/*.jpg")]
filenames =  natsorted(filenames)

print("[INFO] filtering out small blobs started...")
for file in progressbar.progressbar(filenames):
# for file in filenames:
	# Get the filename with extension
	base = os.path.basename(file)
	# print(base)
	# Filename without extension
	filename = os.path.splitext(base)[0]
	# print(filename)

	# Join parent directory and directory that you want to create
	# path = os.path.join(Folder_name, filename)

	# Read the image
	img = cv.imread(file)

	# Convert the image into grayscale
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	# apply basic thresholding -- the first parameter is the image
	# we want to threshold, the second value is is our threshold
	# check; if a pixel value is greater than our threshold (in this
	# case, 230), we set it to be *black, otherwise it is *white*
	ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

	# Find the contours on the gray binary image, and store them in a list
	# Contours are drawn around white blobs.
	# hierarchy variable contains info on the relationship between the contours

	cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
	# ZERO
	# cnts = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key=cv.contourArea, reverse=False)

	for c in cnts:
		cnt_area = cv.contourArea(c)
		# print(cnt_area)
		if cnt_area <=  3000:
			(x, y, w, h) = cv.boundingRect(c)
			thresh[y:y + h, x:x + w] = 0
			cv.imwrite(Folder_name+filename+'.jpg', thresh)
			# cv.rectangle(thresh, (x, y), (x + w, y + h), (0, 0, 255), 1)

		# If there is only one blob
		else:
			cv.imwrite(Folder_name+filename+'.jpg', thresh)

	# cv.namedWindow("[Img]", cv.WINDOW_NORMAL)
	# cv.imshow("[Img]", thresh)
	# cv.waitKey(0)

print("[INFO] filtering our small blobs ended...")

###### Checking total number of blobs after filtering out ##############

filenames = [img for img in glob.glob("Final/*.jpg")]
filenames =  natsorted(filenames)

# for file in progressbar.progressbar(filenames):
for file in filenames:
	# Get the filename witn extension
	base = os.path.basename(file)

	# Filename without extension
	filename = os.path.splitext(base)[0]

	img = cv.imread(file)

	# Convert the image into grayscale
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	# apply basic thresholding -- the first parameter is the image
	# we want to threshold, the second value is is our threshold
	# check; if a pixel value is greater than our threshold (in this
	# case, 230), we set it to be *black, otherwise it is *white*
	ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

	cnts = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key=cv.contourArea, reverse=True)

	ROI = 0
	for c in cnts:
		ROI = ROI + 1
	print("{} = {}".format(filename, ROI))	