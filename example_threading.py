import time
from pms7003 import Pms7003ThreadedReader

if __name__ == '__main__':

    reader = Pms7003ThreadedReader('/dev/serial0')
    reader.start()

    while True:
        print(reader.values)
        time.sleep(1)