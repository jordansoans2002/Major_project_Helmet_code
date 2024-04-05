import cv2
from video_capture import VideoCaptureAsync
import time

vid_w = 1280
vid_h = 720

capture = VideoCaptureAsync(src = 0, width=vid_w, height=vid_h)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

def record_video(duration):
    capture.start()
    time_end = time.time() + duration
    
    frames = 0
    images = []
    
    while time.time() <= time_end:
        ret, new_frame = capture.read()
        frames += 1
        images.append(new_frame)
        
    capture.stop()
    
    fps = frames / duration
    out = cv2.VideoWriter('webcam_vid_'+duration+'_secs.avi',fourcc,fps,(vid_w,wid_h))
    
    for i in range(len(images)):
        out.write(images[i])
    
    images = []