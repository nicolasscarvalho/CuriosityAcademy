from funcs.func_QC import func_QC

def test_voltages_list():
    """
       Checks if the list has 20 items

       This function tests if the generated list of voltages by func_QC.py
       has a size of 20 items.
       """
    try:
        generated_list_voltages = func_QC()
        assert len(generated_list_voltages) == 20
    except ValueError as e:
        assert str(e) == "Voltage > 190."


def test_voltage_error():
    """
        Test function for func_QC.py error handling.

        This function tests whether func_QC generates a ValueError with the message
        "voltage > 190" when a voltage greater than 190 is found in the generated list.
    """
    try:
        func_QC()
    except ValueError as e:
        assert str(e) == "Voltage > 190."
    else:
        raise AssertionError("Expected ValueError was not raised")








