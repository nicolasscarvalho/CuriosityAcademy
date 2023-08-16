from client import Client, serial
from instrument import Instrument

def test_QD():

    client: Client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    data_dictionary = {
        "temperature": [instrument.temperature],
        "voltage": [instrument.voltage],
        "status": [instrument.status],
        "type": [instrument.type],
        "current": [instrument.current],
    }


    return data_dictionary
