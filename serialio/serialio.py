import threading

import serial


class SerialIO(serial.Serial):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__readlock = threading.Lock()

    # This re-definition of read() matches the interface of io.RawIOBase.read().
    # See https://github.com/pyserial/pyserial/issues/585.
    def read(self, size=-1):
        with self.__readlock:
            size = self.in_waiting if size < 0 else min(size, self.in_waiting)
            size = size or 1
            return super().read(size)
