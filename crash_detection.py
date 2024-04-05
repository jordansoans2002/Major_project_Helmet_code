import mpu6050
import time

mpu6050 = mpu6050.mpu6050(0x68)

def read_sensor_data():
    a = mpu6050.get_accel_data()

    g = mpu6050.get_gyro_data()
  
    t = mpu6050.get_temp()
    
    return a, g, t
  
while True:
    # a, g, t = read_sensor_data()
    a = mpu6050.get_accel_data()

    g = mpu6050.get_gyro_data()
  
    t = mpu6050.get_temp()
    
    print("accelerom_data", a)
    print("gyRO", g)
    print("temp", t)
    print("----------")

    time.sleep(1)
    
    