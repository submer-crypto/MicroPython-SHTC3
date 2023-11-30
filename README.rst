Introduction
============

A helper library for using the Senserion SHTC3 Humidity and Temperature Sensor forked from `adafruit/Adafruit_CircuitPython_SHTC3 <https://github.com/adafruit/Adafruit_CircuitPython_SHTC3>`_ and modified to work with **MicroPython 1.19.1**.


Usage Example
=============

.. code-block:: python3

    import time
    import machine
    import shtc3

    i2c = machine.I2C(0)  # uses default SCL and SDA
    sht = shtc3.SHTC3(i2c)

    while True:
        temperature, relative_humidity = sht.measurements
        print("Temperature: %0.1f C" % temperature)
        print("Humidity: %0.1f %%" % relative_humidity)
        print("")
        time.sleep(1)


Documentation
=============

API documentation for the original Adafruit library can be found on `Read the Docs <https://docs.circuitpython.org/projects/shtc3/en/latest/>`_.
