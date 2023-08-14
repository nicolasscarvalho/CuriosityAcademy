from client import Client
import serial

from instrument import Instrument

def test_QB():
    """
    Checks if temperatures are greater than 80 degrees.

    It simulates 20 times the creation of an instrument for a client, 
    where he requests the temperature of the equipment, storing it in a list. 
    At the end, the test checks whether each temperature is greater than 80 degrees; 
    If so, an error is generated.

    Raises:
        DANGEROUS temperature: If temperature > 80 
    """
    client: Client = Client(serial.Serial('COM1', 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial('COM2', 9600, timeout=2))

    temperatures = []

    for i in range(1, 21):

        client.write_request('TMP')
        instrument.read_message()
        temperature: int = int(client.read_response())
        
        temperatures.append(temperature)

    for temperature in temperatures:
        if temperature > 80:
            ValueError('DANGEROUS temperature')
        else:
            print('OK Temperature')