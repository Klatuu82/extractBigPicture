import numpy as np
import cv2
import scipy.misc as smp

data = np.zeros((1, 1, 3), dtype=np.uint8)


def video_to_frames(video_filename, threshold):
    """Extract frames from video"""
    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    pic_h = video_length * threshold
    global data
    data = np.zeros((pic_h, 1920, 3), dtype=np.uint8)
    if cap.isOpened() and video_length > 0:
        count = 0
        success, image = cap.read()
        while success:
            for i in reversed(range(threshold)):
                data[pic_h-(count*threshold)-(threshold-i)-1] = image[i]

            success, image = cap.read()
            count += 1


video_to_frames("resource\\Yiruma-RiverFlowsinYou.mp4", 10)

img = smp.toimage( data )       # Create a PIL image
# img.save("Yiruma-RiverFlowsinYou.jpg")
img.show()
