# A minimalistic python interface for PMS7003 sensor

The code reads PM values from serial port. Tested on Raspberry Pi, but it should work on any machine with Python and serial port.

Device description: <https://aqicn.org/sensor/pms5003-7003/>

## Setup

To install the driver, simply do:
```bash
pip3 install pms7003
```

## Usage example

```python
from pms7003 import Pms7003Sensor, PmsSensorException

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')

    while True:
        try:
            print(sensor.read())
        except PmsSensorException:
            print('Connection problem')

    sensor.close()
```

The read function has an option of returning values as a dict or OrderedDict.

```python
sensor.read(ordered=True)
```

## Usage example with threading:

```python
import time
from pms7003 import Pms7003Thread

if __name__ == "__main__":

    with Pms7003Thread("/dev/serial0") as sensor:

        while True:
            print(sensor.measurements)
            # We're free to do computation in main thread 
            a = 2**32
            time.sleep(1)
```

