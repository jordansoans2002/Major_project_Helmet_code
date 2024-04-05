from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 60
raw_capture = PiRGBArray(camera, size=(640,480))

time.sleep(0.1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'pi_video.avi'
frame_rate = 15
frame_size = (640,480)

images = []
frames = 0
duration =1
end_time = time.time() + duration

# set timer for video to stop
for frame in camera.capture_continous(raw_capture,format='bgr',use_video_port=True):
    if time.time() >= end_time:
        break
    frames += 1
    images.append(frame.array)
    
video_writer = cv2.VideoWriter(output_file,fourcc,frame_rate,frame_size)
video_writer.release()
    