import cv2
import numpy as np
import argparse
import pdb


pdb.set_trace()

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--origin", required=True, help="Path to the original image")
ap.add_argument("-p", "--patch", required=True, help="Path to the patch image")
args = vars(ap.parse_args())
originpath = args["origin"]
patchpath = args["patch"]
 
# all channel for displaying purpose
parent = cv2.imread(originpath)
child = cv2.imread(patchpath)

# only read one channel for matching 
img = cv2.imread(originpath,0)

imgbackup = img.copy()
template = cv2.imread(patchpath,0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
print 'Will use 4 methods to find matches...'
methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
font = cv2.FONT_HERSHEY_SIMPLEX

for meth in methods:
    tmpparent = parent.copy()
    img = imgbackup.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    #calculate difference: top_left=(xmin,ymin) | bottom_right=(xmax,ymax)

    matched = parent[top_left[1]:(bottom_right[1]), top_left[0]:(bottom_right[0]) ]
    difference = sum(sum(sum(matched-child)))
    if difference != 0:
       print 'not exact match with'+' '+meth+' '+'pixel diff:'+ str(difference)
    else:
       print 'exact match found with'+' '+meth

    cv2.rectangle(tmpparent,top_left, bottom_right, (0,0,255), 2)
    cv2.putText(tmpparent,meth, (top_left[0]-10, top_left[1]-10), font, 1,(0,255,0),1,cv2.LINE_AA)
    cv2.imshow('ROI',tmpparent)
    cv2.waitKey(0)	

cv2.destroyAllWindows()
