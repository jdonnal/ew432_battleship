from typing import Tuple
from random import randint
import serial
import time


def host_serial_server(port) -> Tuple[int, serial.Serial]:
    """
    Host a battleship server on the specified serial port
    Uses priority 0
    """

    # create a Serial object associated with the specified port
    device = serial.Serial(port)

    # send synchronization messages until a response is received
    # to connect the client waits until it sees a message and then repeats it back to the server
    # note: this is not fool proof, if the client does not reply correctly we just crash
    while True:
        # synchronization is a random number between 0-1000
        server_syn = randint(0, 1000)
        server_syn_str = "%d\n" % server_syn
        server_syn_bytes = server_syn_str.encode('ascii')
        device.write(server_syn_bytes)
        # wait to see if a client has replied
        time.sleep(0.5)
        if device.in_waiting > 0:
            # yes, a client replied, validate the message
            client_ack_bytes = device.readline()
            client_ack_str = client_ack_bytes.decode('ascii')
            client_ack = int(client_ack_str)
            if client_ack == server_syn:  # valid acknowledgement?
                return 0, device
            else:
                # corrupt response, client is not synchronized
                raise Exception("ERROR: client did not ack")


def connect_serial_client(port) -> Tuple[int, serial.Serial]:
    """
    Connect to a battleship server on the specified serial port
    Uses priority 3
    """
    # --------- BEGIN YOUR CODE ----------

    # create a Serial object associated with the specified port

    # listen for a synchronize message

    # acknowledge the synchronize message

    return 3, None  # <-- replace None with the Serial object
    # --------- END YOUR CODE ----------
