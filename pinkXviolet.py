import tinytuya
import time
import json

DEVICEID = "DEVICEID"
DEVICEIP = "DEVICEIP"
DEVICEKEY = "DEVICEKEY"
DEVICEVERS = "3.3"

# Connect to Tuya BulbDevice

d = tinytuya.BulbDevice(DEVICEID, DEVICEIP, DEVICEKEY)
d.set_version(float(DEVICEVERS)) # IMPORTANT to always set version 
# Keep socket connection open between commands
d.set_socketPersistent(True)


d.set_colour(255, 0, 136)