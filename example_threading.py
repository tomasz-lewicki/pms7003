import time
from threading import Thread, Lock
from pms7003 import Pms7003Sensor, PmsSensorException

class Pms7003Thread(Thread):
    def __init__(self, serial_device):
        super(Pms7003Thread, self).__init__()

        self._sensor = Pms7003Sensor(serial_device)
        self._sensor_lock = Lock()

        self._values = None
        self._values_lock = Lock()

        self._running = True

    # Stuff for context manager
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self._running = False
        with self._sensor_lock:
            self._sensor.close()

    def run(self):
        while self._running:
            
            with self._sensor_lock:
                values = self._sensor.read()

            with self._values_lock:
                self._values = values

            time.sleep(.5) # 2Hz (the sensor has 1Hz update)

    @property
    def values(self):
        with self._values_lock:
            val = self._values
        return val


if __name__ == "__main__":

    with Pms7003Thread("/dev/serial0") as sensor:

        while True:
            print(sensor.values)
            # We're free to do computation in main thread 
            a = 2**32
            time.sleep(1)
