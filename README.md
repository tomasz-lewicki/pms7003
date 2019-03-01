A minimalistic python interface for PMS7003 sensor
https://aqicn.org/sensor/pms5003-7003/

The code reads PM values from serial port. I run it on raspberry Pi, but it should work on any machine with python and serial port.

Usage example:
```python
from pms7003 import Pms7003Sensor, PmsSensorExcpetion

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        try:
            print(sensor.read())
        except PmsSensorExcpetion:
            print('Connection problem')
```

The read function has an option of returning values as a dict or OrderedDict
```python
sensor.read(ordered=True)
```
