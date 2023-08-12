from client import Client
from instrument import Instrument
import serial

def test_QA():

    serial_config = serial.Serial(port='COM1')

    client: Client = Client(ser=serial_config)
    instrument: Instrument = Instrument(ser=serial_config)