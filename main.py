import numpy as np
import cv2
import scipy.misc as smp
import pytube
import os

'''
Cute the image in to 10000 line hight images insted of i big.
'''
fixedhight = 10000
images = []
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
    global data
    data = np.zeros((fixedhight, 1920, 3), dtype=np.uint8)
    if cap.isOpened() and video_length > 0:
        count = 0
        success, im_cv = cap.read()
        image = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)


        while success:
            for i in reversed(range(threshold)):
                data[fixedhight-(count*threshold)-(threshold-i)-1] = image[i]


            success, im_cv = cap.read()
            if success:
                image = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
            count += 1
            if count*threshold % 10000 == 0:
                images.append(data)
                data = np.zeros((fixedhight, 1920, 3), dtype=np.uint8)
                count = 0


def saveimg(title):
    os.makedirs(title)
    count = 0
    for im_data in images:
        img = smp.toimage( im_data )       # Create a PIL image
        img.save("./" + title + "/" + str(count) + title+".jpg")
        count += 1




print("Get Video")

videoTitle = getVideo('https://www.youtube.com/watch?v=NPBCbTZWnq0')
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



