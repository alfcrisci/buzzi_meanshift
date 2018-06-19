import os, sys
import cv2
import pymeanshift as pms
import scipy.misc

# get the arguments

# https://github.com/fjean/pymeanshift 

InRaster = sys.argv[1]
OutRaster = sys.argv[2]
spatial_radius  = int(sys.argv[3])
range_radius  = float(sys.argv[4])
min_density = int(sys.argv[5])

original_image=cv2.imread(InRaster)

(segmented_image, labels_image, number_regions) = pms.segment(original_image, spatial_radius=spatial_radius, 
range_radius=range_radius,                  
min_density=min_density)

scipy.misc.imsave(OutRaster, segmented_image)



