### First program python_show_img.py will read 
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

### Second program will pick one line from 
```bash
BBox_List_2017.csv 
```
and read coresponding image and plot given bounding box
```bash
python python_show_box.py
```

### Third program allows you to select a 
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
