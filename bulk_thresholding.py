"""
Project: How to threshold the image in a bulk?
Author: Yonten Jamtsho
Date Created: September 4, 2021
Description: This project will threshold all the images using OpenCV
"""

# Import library
import cv2 as cv
from natsort import natsorted
import glob
import numpy as np
import os
import progressbar

# Path to the output folder
Folder_name = "Thresholded/"

filenames = [img for img in glob.glob("Dataset/*.jpg")]
filenames =  natsorted(filenames)

print("[INFO] thresholding started...")
for file in progressbar.progressbar(filenames):
	# Get the filename with extension
	base = os.path.basename(file)

	# Filename without extension
	filename = os.path.splitext(base)[0]
	# print(filename)

# 	# Join parent directory and directory that you want to create
	# path = os.path.join(Folder_name, filename)

	# Read image
	img = cv.imread(file)
	# print(img.shape)

	# Convert to grayscale
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	# print(gray.shape)

	# apply basic thresholding -- the first parameter is the image
	# we want to threshold, the second value is is our threshold
	# check; if a pixel value is greater than our threshold (in this
	# case, 230), we set it to be *black, otherwise it is *white*
	ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY_INV)
	cv.imwrite(Folder_name+filename+'.jpg', thresh)

print("[INFO] thresholding finished...")