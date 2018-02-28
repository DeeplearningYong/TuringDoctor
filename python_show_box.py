import sys #its used to read arguments
import cv2 #to import opencv packages so we can use opencv functions, you can google what is opencv  
import pdb #python debugger so you can run python program line by line to understand it  
import csv #python csv packages to read csv files 

def showgivenimg (imgname, x,y,w,h):
        print "This is the name of image you want to view: ", imgname  # print your image name
        pathToImg = '/Users/davidli/TuringDoctor/images/'+ imgname #path to the image
        img = cv2.imread(pathToImg)   #read into opencv

        #print 'press any key to continue to next cropped image'
        #cv2.imshow('original',img) #opencv can show the image
        #cv2.waitKey(0)  #google opencv waitkey function to understand what it means
        print "press any key to close program"

        crop_img = img[y:y+h, x:x+w]  #only take portion of the image, it cuts from top left [x,y] till bottom right of [x+w, y+h] where w is width, h is height
	
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow('original with box', img)
        cv2.waitKey(0)

	cv2.imshow('cropped', crop_img)
        cv2.waitKey(0)


        return;

with open("BBox_List_2017.csv", "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
	#pdb.set_trace()
	if i == 13:
	        print i, line[0].split(',')[0]
		pdb.set_trace()
		imgname = line[0].split(',')[0]
		label = line[0].split(',')[1]
		x = line[0].split(',')[2]
		y = line[0].split(',')[3]
		width = line[0].split(',')[4]
		height = line[0].split(',')[5]
		showgivenimg(imgname, int(float(x)), int(float(y)), int(float(width)), int(float(height)))



