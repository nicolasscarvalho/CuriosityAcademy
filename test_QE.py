from client import Client, serial
from instrument import Instrument

def test_QE():
    """
    Simulates connecting to an instrument and gets 30 random voltages
    in the range of ]25mA, 800mA[. if voltage < 25mA, print a message.

    returns:
        voltage list(int): List with the voltage values
    """ 
    client: Client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))
    
    voltages = []
    
    for _ in range(0, 30):
        client.write_request('VOL')
        instrument.read_message()
        
        voltage: int = int(client.read_response())
        
        if voltage < 25.0:
            print(f'Threshold alert! ({voltage}mA)')
        elif voltage < 800.0:
            voltages.append(voltage)
            
    return voltages 