import serial
from client import Client
from instrument import Instrument

def test_QC():
    """
    Simulates connecting to an instrument and gets 20 random voltages in a list.

    returns:
        voltage list(int): List with voltages.
    """
    client: Client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    voltages = []

    for i in range(1, 21):
        client.write_request("VOL")  
        instrument.read_message()    
        voltage: int = int(client.read_response())  

        voltages.append(voltage)

    print("Voltages:", voltages)

    for voltage in voltages:
        if voltage == 0:
            print("Voltage = 0.")

        if voltage > 190:
            raise ValueError("Voltage > 190.")

    return voltages