# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import time
import machine
import shtc3

i2c = machine.I2C(0)  # uses default SCL and SDA
sht = shtc3.SHTC3(i2c)

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature) # pylint: disable=consider-using-f-string
    print("Humidity: %0.1f %%" % relative_humidity) # pylint: disable=consider-using-f-string
    print("")
    time.sleep(1)
