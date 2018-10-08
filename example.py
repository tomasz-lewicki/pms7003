from pms7003 import Pms7003Sensor

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        print(sensor.read())