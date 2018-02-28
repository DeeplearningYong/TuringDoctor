import cv2
import numpy as np
import pdb


pdb.set_trace()

img = cv2.imread('/Users/davidli/TuringDoctor/images/00000001_000.png',0)
cv2.rectangle(img, (100,100), (300,300), (0,0,255),3)

cv2.imshow('ROI',img)
cv2.waitKey(0)

img2 = img.copy()
template = cv2.imread('disease1.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
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
    
    pdb.set_trace()
    cv2.rectangle(img,top_left, bottom_right, (0,255,255), 2)
    cv2.imshow('ROI',img)
    cv2.waitKey(0)	

    #plt.subplot(121),plt.imshow(res)
    #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(img)
    #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #plt.suptitle(meth)

    #plt.show()

