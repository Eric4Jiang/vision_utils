import cv2
import numpy as np
import numbers
import decimal
import logging

from networktables import NetworkTables

# Inits NetworkTable. If no arguments are passed, default values will be used. 
#
# Argments:
#   *server: server IP address or hostname you're connecting you as a client.
#   *key: name of NetworkTable instance.
#
# Returns: NetworkTable instance of specified key.
def initTable(server="10.3.34.50", key="vision"):
    # necessary to see networkTables
    logging.basicConfig(level=logging.DEBUG)

    print("Initialized NetworkTables ", NetworkTables.initialize(server))
    nt = NetworkTables.getTable(key)

    return nt

# Send data values to a NetworkTable.
#
# Arguments:
#   *nt = a NetworkTable instance.
#   *data = values (any type) to put on nt. Stored as a dictionary:
#           { key1 : value1, key2 : value2, ...}
def sendData(nt, data):
    for key, value in data.iteritems():
        print ("key", key, "value", value)
        if isinstance(value, bool):
            nt.putBoolean(key, value)
        elif isinstance(value, numbers.Number):
            nt.putNumber(key, value)
        elif isinstance(value, str):
            nt.putString(key, value)
