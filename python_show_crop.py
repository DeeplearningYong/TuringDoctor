import cv2
import argparse
import numpy as np
import sys
import pdb
 
if __name__ == '__main__' :
 
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
    imgname = args["image"].split('/')[1].split('.')[0]
	
    #pdb.set_trace() 
    im = cv2.imread(args["image"])
     
    # Select ROI
    fromCenter = False
    r = cv2.selectROI(im, fromCenter)
     
    # Crop image
    # y:y+height, x:x+width 
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    xmin = int(r[0])
    ymin = int(r[1])
    xmax = int(r[0]+r[2])
    ymax = int(r[1]+r[3])
 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)

    var = raw_input("Please enter name of the region: ")
    imgcropname = imgname+'_'+var+'.png'
    cv2.imwrite(imgcropname,imCrop)

    txtoutname = imgname+'_'+var+ '.txt'
    bboxfile = open(txtoutname,'w')
    
    #pdb.set_trace()
    
    # disease type | xmin | ymin | xmax | ymax 
    tmpstr = var+ ' '+ str(xmin)+' '+str(ymin)+' '+str(xmax)+' '+str(ymax)
    bboxfile.write(tmpstr) 
    bboxfile.close()

    cv2.destroyAllWindows()

