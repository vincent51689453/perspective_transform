import cv2
import transform
import numpy as np

image_path = 'samples/input/road3.jpg'

# Results using camer calibration
camera_matrix = np.array([[2043.94561663, 0.00000000,   03.97714629]
,[0.00000000,   2065.70880726, 716.14154624]
,[0.00000000,  0.00000000,   1.00000000  ]], dtype = "float32")

distortion_matrix = np.array([[0.365169490972,-1.573638145364,0.045580840817,0.029492347585,3.737781798978]], dtype = "float32")

print("Camera Matrix:",camera_matrix)
print("Distortion Coef:",distortion_matrix)

def points_init():
    # You can use check_cord.py to find your desired ROI
    top_left = (260,140)
    top_right = (410,140)
    bottom_right = (560,480)
    bottom_left = (110,480)

    points = []
    points.append(top_left)
    points.append(top_right)
    points.append(bottom_right)
    points.append(bottom_left)

    return points

def draw_anchors(image_vis,points):
    cv2.line(image_vis, (points[0][0],points[0][1]), (points[1][0],points[1][1]), (0, 0, 255), 2)
    cv2.line(image_vis, (points[0][0],points[0][1]), (points[3][0],points[3][1]), (0, 0, 255), 2)
    cv2.line(image_vis, (points[1][0],points[1][1]), (points[2][0],points[2][1]), (0, 0, 255), 2)
    cv2.line(image_vis, (points[2][0],points[2][1]), (points[3][0],points[3][1]), (0, 0, 255), 2)

    cv2.circle(image_vis,(points[0][0],points[0][1]), 5, (0, 255, 0), -1)
    cv2.circle(image_vis,(points[1][0],points[1][1]), 5, (0, 255, 0), -1)
    cv2.circle(image_vis,(points[2][0],points[2][1]), 5, (0, 255, 0), -1)
    cv2.circle(image_vis,(points[3][0],points[3][1]), 5, (0, 255, 0), -1)
    return image_vis


# Read image
anchors = points_init()
image = cv2.imread(image_path)
image_bk = image

# Perspective transformation
image = transform.bird_view_transform_4pts(image, anchors)
image_undist = transform.distortion_remove(image, camera_matrix, distortion_matrix)
cv2.imshow("Transform Result",image_undist)

# Anchor visualization
image_vis = draw_anchors(image_bk,anchors)
cv2.imshow("anchors",image_vis)
cv2.imwrite('samples/output/road2_output.jpg',image)

cv2.waitKey(0)
