import time
from pms7003 import Pms7003Thread


if __name__ == "__main__":

    with Pms7003Thread("/dev/serial0") as sensor:

        while True:
            print(sensor.measurements)
            # We're free to do computation in main thread 
            a = 2**32
            time.sleep(1)
