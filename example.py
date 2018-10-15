from pms7003 import Pms7003Sensor, PmsSensorExcpetion

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        try:
            print(sensor.read())
        except PmsSensorExcpetion:
            print('Connection problem')

