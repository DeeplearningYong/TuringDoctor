### (1) First program python_show_img.py will read 
```bash
00000001_000.png 
```
from images folder and show original image, then show a rectangular area of 
```bash
[x=100, y=200] with width 300, height 400 
```
![alt text](http://math.hws.edu/eck/cs124/javanotes6/c6/gui_coordinates.png)
```bash
python python_show_img.py 00000001_000 100 200 300 400
```

### (2) Second program will pick one line from 
```bash
BBox_List_2017.csv 
```
and read coresponding image and plot given bounding box
```bash
python python_show_box.py
```

### (3) Third program allows you to select a 
```bash
bounding box 
```
from the image, then ask you to give 
```bash
region name
```
then write cropped region into a image file and txt file
```bash
python python_show_crop.py --image images/00000001_000.png
```

### (4) Doctor can use any program to cut the interested region from the image, e.g., use Preview on MAC, then name the cutted image as original name plus some disease type
this program can be used to find where it was cutted:
```bash
# --o gives the origin image, --p gives the image you want to find whether it was cutted from origin image or not
python python_show_match.py --o images/00000001_000.png --p 00000001_000_disease1.png
```
You will observer output as following if matches is found:
```bash
Will use 4 methods to find matches...
exact match found with cv2.TM_CCOEFF_NORMED
exact match found with cv2.TM_CCORR_NORMED
exact match found with cv2.TM_SQDIFF
exact match found with cv2.TM_SQDIFF_NORMED
```
or 
