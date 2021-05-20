# SerialIO

pySerial's `Serial` class inherits from `io.RawIOBase`, but its implementation of `read()` doesn't follow the [specification's interface](https://docs.python.org/3/library/io.html#io.RawIOBase.read):

> **read**(*size=-1*)  
> Read **up to** *size* bytes from the object and return them.

Instead, `Serial.read()` reads **exactly** *size* bytes.

Because this is a fundamental, low-level method, virtually all of the other layers of the I/O hierarchy break down due to this behavior.

This module introduces a `SerialIO` subclass of `pySerial.Serial` that re-implements `read()` to match the semantics of `io.RawIOBase.read()`.
