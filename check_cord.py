import cv2

image_path = 'samples/input/road2.jpeg'


def pixel_picker(event,x,y,flag,param):
    global phase,points
    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouseX:{} mouseY:{}".format(x,y))
            

# Read image
image = cv2.imread(image_path)

# Mouse Picker
cv2.imshow("input",image)
cv2.setMouseCallback("input",pixel_picker)

cv2.waitKey(0)