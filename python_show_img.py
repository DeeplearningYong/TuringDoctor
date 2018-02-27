import sys # its used to read arguments
import cv2 # to import opencv packages so we can use opencv functions, you can google what is opencv  
import pdb # python debugger so you can run python program line by line to understand it  

#pdb.set_trace() # set a breakpoint so your program will stop here, then you type n to run it line by line 

print "This is the name of image you want to view: ", sys.argv[1]  # print your image name 

pathToImg = '/Users/davidli/TuringDoctor/images/'+ sys.argv[1]+'.png' #path to the image 
img = cv2.imread(pathToImg)   #read into opencv 

print 'press any key to continue to next cropped image'

cv2.imshow('original',img) #opencv can show the image 
cv2.waitKey(0)  #google opencv waitkey function to understand what it means 

print "press any key to close program" 

x = int(sys.argv[2])
y = int(sys.argv[3])
w = int(sys.argv[4])
h = int(sys.argv[5])

crop_img = img[y:y+h, x:x+w]  #only take portion of the image, it cuts from top left [x,y] till bottom right of [x+w, y+h] where w is width, h is height
cv2.imshow('cropped', crop_img)
cv2.waitKey(0)


