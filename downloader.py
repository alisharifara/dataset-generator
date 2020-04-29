import cv2
import os
import os.path
from os import path
from pytube import YouTube
import time
from PIL import Image

def get_videos(paths):
    for i in range(0, len(paths)):
        file_name = "videos/" + paths[i].rsplit('/', 1)[-1] + ".mp4"
        if not os.path.isfile(file_name):
            file_orig = YouTube(paths[i]).streams.get_highest_resolution().download()
            os.rename(file_orig, file_name)
            print(file_name + ' downloaded.')
        else:
            print(file_name + ' skipped.')

def get_frames(paths, cnt):
   for i in range(0, cnt):
        file_name = "images/" + paths[i].rsplit('/', 1)[-1]
        if not os.path.exists(file_name):
            os.makedirs(file_name)
            time_start = time.time()
            count = 100
            cap = cv2.VideoCapture("videos/" + paths[i].rsplit('/', 1)[-1] + ".mp4")
            video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
            print ("Total number of frames: ", video_length)
            print ("Converting video...\n")
    
            while cap.isOpened():
                # Extract the frame
                ret, frame = cap.read()
                if count % 5 ==0 and count >500:
                    cv2.imwrite(file_name + "/%#05d.jpg" % (count+1), frame)
                count +=1

                if (count+200 > (video_length-1)):
                    time_end = time.time()
                    cap.release()
                    #count = count/1
                    print ("Done extracting frames.\n%d frames extracted" % count)
                    print ("It took %d seconds for conversion." % (time_end-time_start))
                    break
        else:
            print(file_name + ' skipped.')        

def main():

    links = ['']

    print('********** Going to download videos *************')
    get_videos(links)
    print('********** Going to extract frames *************')
    get_frames(links,len(links))
    print('********** !!!DONE!!! *************')

if __name__ == "__main__":
    main()
