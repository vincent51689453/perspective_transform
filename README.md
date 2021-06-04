# perspective_transform
It helps to transform the camera's view into bird's eye view.

### How to use (Image)
1. Check anchor coordinates using check_cord.py
Put the picture in samples/input/ and change the file path in check_cord.py.

Remeber there is a sequence to take the coordinates which are top left -> top right -> bottom right -> bottom left. After getting all these numbers you can start modify main_image.py.

2. Modify main_image.py
Chagen the file path in main_image.py

It depends on the camera you are using. The camera matrix and distortion coefficients should be changed according to the properties of your camera model. Afterward, you can fill in all the anchors' coodinates in points_init().

### Output
Two images are generated as the output of main_image.py. They are stored in samples/output. 

