from client import Client
import serial

from instrument import Instrument

def test_QA():
    """
    Simulates connecting to an instrument and gets 20 random temperatures

    returns:
        temperature list(int): List with temperatures
    """
    client: Client = Client(serial.Serial('COM1', 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial('COM2', 9600, timeout=2))

    temperatures = []

    for i in range(1, 21):

        client.write_request('TMP')
        instrument.read_message()
        temperature: int = int(client.read_response())
        
        temperatures.append(temperature)

    return temperatures