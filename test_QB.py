from client import Client
from instrument import Instrument
import serial

def test_QB():

    serial_config = serial.Serial(port='COM3')
    client: Client = Client(ser=serial_config)

    temperatures = []

    for i in range(1, 21):
        instrument: Instrument = Instrument(ser=serial_config)

        client.write_request('TMP')
        instrument.read_message()

        temperatures.append( int(client.read_response()) )

    for temperature in temperatures:
        assert temperature > 80