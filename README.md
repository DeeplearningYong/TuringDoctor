### Turing-AI-Doctor Tasks:
1.a) label bounding boxes for 110k images <\br>
1.b) 1st model => image => no findings or have findings
---Alexnet
---VGGnet
---Resnet
2) 2nd model => image => no findings or some diseases from 14 category
3) 3rd model => image => bounding box with diagnosis 
---SSD
---Faster R-CNN|Mask R-CNN

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
with output:
```bash
python python_show_crop.py --image images/00000001_000.png
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Please enter name of the region: disease1
```
and you will find 00000001_000_disease1.png and 00000001_000_disease1.txt in your current working folder. you can modify the save path to other places. 
You can create several outputs so you can use it in the next step. 

### (4) Doctor can use any program to cut the interested region from the image,
###### e.g., use Preview on MAC, then name the cutted image as original name plus some disease type
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
```bash
python python_show_match.py --o images/00000001_000.png --p 00000001_001_disease2.png
```
with output:
```bash
Will use 4 methods to find matches...
not exact match with cv2.TM_CCOEFF_NORMED pixel diff:642
not exact match with cv2.TM_CCORR_NORMED pixel diff:102
not exact match with cv2.TM_SQDIFF pixel diff:486
not exact match with cv2.TM_SQDIFF_NORMED pixel diff:102
```
when not exact matches was found. 
