from pms7003 import Pms7003Sensor, PmsSensorException

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        try:
            print(sensor.read())
        except PmsSensorException:
            print('Connection problem')

    sensor.close()
