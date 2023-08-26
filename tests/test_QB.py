from funcs.func_QA import func_QA
from funcs.func_QB import func_QB

def test_QB():
    """
    Verifies instrument temperature safety.

    If less than or equal to 80, it returns "OK TEMPERATURE", 
    if not, it returns DANGEROUS temperature
    """

    temperatures: list[int] = func_QA()

    for temperature in temperatures:
        assert func_QB(temperature) == "OK Temperature"