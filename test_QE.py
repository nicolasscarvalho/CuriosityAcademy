from client import Client, serial
from instrument import Instrument

def test_QE():
    """
    Simulates connecting to an instrument and gets 30 random currents
    in the range of ]25mA, 800mA[. If voltage < 25mA, print a message.

    returns:
        currents list(int): List with the voltage values
    """ 
    client: Client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument: Instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))
    
    currents = []
    
    for _ in range(0, 30):
        client.write_request('CUR')
        instrument.read_message()
        
        current: int = int(client.read_response())
        
        if 25 < current < 800:
            currents.append(current)
        elif current < 25:
            print(f'Threshold alert! ({current}mA)')
            
    return currents
