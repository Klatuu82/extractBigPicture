import numpy as np
import cv2
import scipy.misc as smp
import pytube
import os

def getVideo(url):
    # url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(file_extension='mp4', fps=30, res='1080p').order_by('resolution').first()
    video.download('./temp')
    return video.title


data = np.zeros((1, 1, 3), dtype=np.uint8)


def extract_data(video_filename, threshold):
    """Extract frames from video"""
    if not os.path.exists(video_filename):
        print("File not Found")
        return

    cap = cv2.VideoCapture(video_filename)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    pic_h = video_length * threshold
    global data
    data = np.zeros((pic_h, 1920, 3), dtype=np.uint8)
    if cap.isOpened() and video_length > 0:
        count = 0
        success, im_cv = cap.read()
        image = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)


        while success:
            for i in reversed(range(threshold)):
                data[pic_h-(count*threshold)-(threshold-i)-1] = image[i]

            success, im_cv = cap.read()
            if success:
                image = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
            count += 1


def saveimg(title):
    img = smp.toimage( data )       # Create a PIL image
    img.save(title+".jpg")
    img.show()




print("Get Video")

videoTitle = getVideo('https://www.youtube.com/watch?v=b8HVQtIoBYU')
videoTitlePath = os.path.abspath('./temp/' + os.listdir('./temp')[0])

print("Video: " + videoTitle + " saved. \nTry to extract Imagedata:")
if not os.path.exists(videoTitlePath):
    print("File not Found")
    exit(1)
extract_data(videoTitlePath, 10)
print("Saving Imagefile:")
saveimg(videoTitle)
print("Removing Video:")
os.remove(videoTitlePath)



