import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

index = 0

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    key = cv.waitKey(1)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if key == ord('q'):
        break
    if key == ord('x'):
        save_path = './samples/input/img_' + str(index) + '.jpg'
        cv.imwrite(save_path,frame)
        print("saved:",save_path)
        index += 1

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
