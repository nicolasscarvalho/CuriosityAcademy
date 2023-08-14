import serial

class Client:
    """
    Simulated client class that reads and writes messages to a serial port.

    This class simulates an client that communicates with a instrument through a serial port.
    It can read messages from the serial port and test the response accordingly.

    Args:
        ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
    """

    def __init__(self, ser: serial.Serial) -> None:
        """
        Initialize the Client with a serial port.

        Args:
            ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
        """
       
        self.ser = ser

    def read_response(self) -> str:
        """
        Read a message from the serial port and returns the response.

        Returns:
            response (str): the response from instrument 
        """

        message = self.ser.readline().decode()
        response = message[:3]

        return response
    
    def write_request(self, request: str) -> None:
        """
        Write a request to the serial port.

        This method writes a request to the serial port. The request is sent as bytes
        using the UTF-8 encoding.

        Args:
            request (str): The request to be sent.
        """

        self.ser.write(bytearray(request + "\r\n", 'utf-8'))