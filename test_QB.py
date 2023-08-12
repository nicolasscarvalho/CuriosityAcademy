from client import Client
from instrument import Instrument
import serial

def test_QB():

    serial_config = serial.Serial(port='COM1')

    client: Client = Client(ser=serial_config)
    instrument: Instrument = Instrument(ser=serial_config)