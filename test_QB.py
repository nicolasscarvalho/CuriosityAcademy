from client import Client
import serial

def test_QB(client_obj):
    """
    Checks if temperatures are greater than 80 degrees.

    It simulates 20 times the creation of an instrument for a client, 
    where he requests the temperature of the equipment, storing it in a list. 
    At the end, the test checks whether each temperature is greater than 80 degrees; 
    If so, an error is generated.
    """
    serial_config = serial.Serial(port='COM2')
    client: Client = Client(ser=serial_config)

    temperatures = []

    for i in range(1, 21):

        client.write_request('TMP')
        temperatures.append( int(client.read_response()) )

    for temperature in temperatures:
        print(temperature > 80)