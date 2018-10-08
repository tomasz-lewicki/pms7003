import serial 

class WrongChecksumException(Exception):
    pass

START_SEQ = bytes([0x42, 0x4d])
FRAME_BYTES = 30

VALUES_MEANING = {
1 : 'PM1.0CF1',
2 : 'PM2.5CF1',
3 : 'PM10CF1', 
4 : 'PM1.0',
5 : 'PM2.5',
6 : 'PM10',
7 : 'n0.3',
8 : 'n0.5',
9 : 'n1.0',
10 : 'n5.0',
11 : 'n10',
}

NO_VALUES = len(VALUES_MEANING)


class Pms7003Sensor:

    def __init__(self, serial_device):
        #values according to product data manual
        self._serial = serial.Serial(port=serial_device, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE, timeout=2)

    def _get_frame(self):
        with self._serial as s:
            s.read_until(START_SEQ)
            return list(s.read(FRAME_BYTES)) #return frame as a list of ints

    def _parse_frame(self, f):
        #iterate every second object and glue the H and L bytes together
        vls = [f[i]<<8 | f[i+1] for i in range(0, len(f), 2)]
        #self._frame_len = vls[0] (you can read the frame length from here)
        return vls

    def _validate_frame(self, vls, frame):
        _checksum = vls[-1]
        if _checksum != sum(frame[:-2]) + sum(START_SEQ):
            raise WrongChecksumException

    def read(self): #returns tuple with measurements or raises WrongCheck
        frame = self._get_frame()
        values = self._parse_frame(frame)
        try:
            self._validate_frame(frame, values)
        except WrongChecksumException:
            #The checksum check failed during parsing the frame
            pass

        return {VALUES_MEANING[i]: values[i] for i in range(1, NO_VALUES)}