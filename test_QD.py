from client import Client
from instrument import Instrument
import serial


def test_QD():

    client: Client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    dictionary = {
        "temperature": [],
        "voltage": [],
        "current": [],
        "status": [],
        "type": [],
        
    }

    for i in range(1, 21):
        client.write_request("TMP")
        instrument.read_message()
        temperature: int = int(client.read_response())
        dictionary["temperature"].append(temperature)

        client.write_request("VOL")  
        instrument.read_message()    
        voltage: int = int(client.read_response())  
        dictionary["voltage"].append(voltage)

        client.write_request('CUR')
        instrument.read_message()
        current: int = int(client.read_response())
        dictionary["current"].append(current)

    
    for i in range(1, 6):
        client.write_request("STA")
        instrument.read_message()
        status: int = int(client.read_response())
        dictionary["status"].append(status)

        client.write_request("TYP") 
        instrument.read_message()
        type: str = str(client.read_response())
        dictionary["type"].append(type)

    return dictionary

