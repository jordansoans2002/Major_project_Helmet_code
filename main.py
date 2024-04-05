from camera_record import record_video
from multiprocessing import Process

record_time = 1

webcam = Process(target = record_video, args = (record_time, ))


webcam.start()

webcam.join()

webcam.close()