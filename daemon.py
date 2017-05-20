#!/usr/bin/env python3
import time
import traceback

import graphitesend

import chirp

graphitesend.init(graphite_server="192.168.1.3", prefix="i2c.chirp")

sensor = chirp.Chirp()

print("Beginning read loop.")

while True:
    # noinspection PyBroadException
    try:
        data = {
            "temp.1": sensor.temp() * 0.1,
            "moist.1": sensor.moist()
        }
    except:
        data = None
        traceback.print_exc()
    if data:
        graphitesend.send_dict(data)
    time.sleep(20)
