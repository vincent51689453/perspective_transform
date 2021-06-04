import cv2
import transform

image_path = 'samples/input/road2.jpeg'


def points_init():
    # You can use check_cord.py to find your desired ROI
    top_left = (436,333)
    top_right = (538,333)
    bottom_right = (884,529)
    bottom_left = (155,529)

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
cv2.imshow("Transform Reulst",image)

# Anchor visualization
image_vis = draw_anchors(image_bk,anchors)
cv2.imshow("anchors",image_vis)




cv2.waitKey(0)