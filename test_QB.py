from client import Client

from instrument import Instrument
from test_QA import test_QA

def test_QB(temperatures):
    """
    Checks if temperatures are greater than 80 degrees.

    Raises:
        DANGEROUS temperature: If temperature > 80 
    """

    for temperature in temperatures:
        if temperature > 80:
            ValueError('DANGEROUS temperature')
        else:
            print('OK Temperature')

temperatures = test_QA()
test_QB(temperatures=temperatures)