"""
Author: Yonten Jamtsho
Date: 26-March-2021
This code will dilate (adding pixels) the image
"""

# Import library
import cv2 as cv
from natsort import natsorted
import glob
import numpy as np
import os
import progressbar

# Path to the output folder
Folder_name = "Dilated/"

filenames = [img for img in glob.glob("Dataset/*.jpg")]
filenames =  natsorted(filenames)

print("[INFO] dilation started...")
for file in progressbar.progressbar(filenames):
	# Get the filename witn extension
	base = os.path.basename(file)
	# print(base)
	# Filename without extension
	filename = os.path.splitext(base)[0]
	# print(filename)

	# Join parent directory and directory that you want to create
	path = os.path.join(Folder_name, filename)

	img = cv.imread(file)

	# Define the kernel size
	kernel = np.ones((3, 3), 'uint8')

	# Dilate the image
	dilate_img = cv.dilate(img, kernel, iterations = 2)
	cv.imwrite(Folder_name+filename+'.jpg', dilate_img)

print("[INFO] dilation finished...")