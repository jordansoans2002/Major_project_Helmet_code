from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import time
import cv2

cam = Picamera2()
video_config = cam.create_video_configuration()
cam.configure(video_config)

encoder = H264Encoder(10000)

cam.start()
cam.start_recording(encoder,'picam2_test.h264')
time.sleep(10)
cam.stop_recording()
cam.close()