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

    rect = np.zeros((4, 2), dtype = "float32")
    rect[0] = top_left
    rect[1] = top_right
    rect[2] = bottom_right
    rect[3] = bottom_left

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
		            [maxW - 1, 0],
		            [maxW - 1, maxH - 1],
		            [0, maxH - 1]], dtype = "float32")

    print(dst)
	# compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    result = cv2.warpPerspective(image, M, (maxW, maxH))

    return result

def distortion_remove(image,camera_matrix,distor_matrix):
    h,w = image.shape[:2]

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distor_matrix, (w, h), 1, (w, h))
    dst = cv2.undistort(image, camera_matrix, distor_matrix, None, newcameramtx)

    # crop and save the image
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    print("Distortion remove")

    return dst