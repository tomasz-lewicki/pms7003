from threading import Thread, Lock
from .pms7003 import Pms7003Sensor
import time

class Pms7003Thread(Thread):
    def __init__(self, serial_device):
        super(Pms7003Thread, self).__init__()

        self._sensor = Pms7003Sensor(serial_device)
        self._sensor_lock = Lock()

        self._m = None
        self._m_lock = Lock()

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
                measurements = self._sensor.read()

            with self._m_lock:
                self._m = measurements

            time.sleep(.5) # 2Hz (the sensor has 1Hz update)

    @property
    def measurements(self):
        with self._m_lock:
            val = self._m
        return val
