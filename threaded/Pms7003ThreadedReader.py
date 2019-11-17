import time
import threading 
from collections import deque
from statistics import mean
from pms7003.pms7003 import Pms7003Sensor, PmsSensorException

class EmptyRaderBufferException(ValueError):
    pass

class Pms7003ThreadedReader(threading.Thread):
    def __init__(self, serial_device, bufsize=1, logger=None):
        super(Pms7003ThreadedReader, self).__init__()

        self._sensor = Pms7003Sensor(serial_device)
        self._value_buffers_lock = threading.Lock()
        self._logger = logger

        def _buffer():
            return deque(maxlen=bufsize)

        self._value_buffers = {'n1_0': _buffer(), 'pm2_5': _buffer(), 'n5_0': _buffer(), 'pm1_0cf1': _buffer(), 'pm1_0': _buffer(), 'n10': _buffer(), 'n0_3': _buffer(), 'pm10': _buffer(), 'n0_5': _buffer(), 'pm2_5cf1': _buffer(), 'pm10cf1': _buffer()}


    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self._sensor.close()

    def run(self):
        while True:
            time.sleep(1)
            try:
                values = self._sensor.read()
    

                self._value_buffers_lock.acquire()
                for k, v in values.items():
                    self._value_buffers[k].append(v)
                self._value_buffers_lock.release() 

            except PmsSensorException as e:
                if self._logger:
                    self._logger.error('{} {}'.format(round(time.time()), e))

    def filtered_values(self):
        self._value_buffers_lock.acquire()
        bufs = self._value_buffers
        self._value_buffers_lock.release()  

        if not all(val for val in bufs.values()):
            raise EmptyRaderBufferException

        return {k: round(mean(d),2) for k, d in bufs.items()}