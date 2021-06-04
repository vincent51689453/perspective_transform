import numpy as np
import cv2


# This function helps to transform a chosen ROI into bird's view
# Be careful about the order of pts
def bird_view_transform_4pts(image,pts):
    # Resultant image
    result = None

    # Format of pts
    # pts[0] -> top left     (x,y)
    # pts[1] -> top right    (x,y)
    # pts[2] -> bottom right (x,y)
    # pts[3] -> bottom left  (x,y)

    top_left = pts[0]
    top_right = pts[1]
    bottom_right = pts[2]
    bottom_left = pts[3]

    # Find width betweeen bottom right/left and top right/left
    widthA = np.sqrt((top_left[0]-top_right[0])**2+(top_left[1]-top_right[1])**2)
    widthB = np.sqrt((bottom_left[0]-bottom_right[0])**2+(bottom_left[1]-bottom_right[1])**2)

    # Find height between top/bottom left and top/bottom right
    heightA = np.sqrt((top_left[0]-bottom_left[0])**2+(top_left[1]-bottom_left[1])**2)
    heightB = np.sqrt((top_right[0]-bottom_right[0])**2+(top_right[1]-bottom_right[1])**2)

    # Find maximum height and width among these points
    maxH = max(int(heightA),int(heightB))
    maxW = max(int(widthA),int(widthB))

    # Destination points after transformation
    dst = np.array([
	            	[0, 0],
		            [maxWidth - 1, 0],
		            [maxWidth - 1, maxHeight - 1],
		            [0, maxHeight - 1]], dtype = "float32")

    
	# compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    result = cv2.warpPerspective(image, M, (maxW, maxH))

    return result