from client import Client
from instrument import Instrument
import serial

def test_QB():
    """
    Checks if temperatures are greater than 80 degrees.

    It simulates 20 times the creation of an instrument for a client, 
    where he requests the temperature of the equipment, storing it in a list. 
    At the end, the test checks whether each temperature is greater than 80 degrees; 
    If so, an error is generated.
    """
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