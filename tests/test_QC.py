from funcs.func_QC import func_QC

def test_voltages_list():
    try:
        generated_list_voltages = func_QC()
        assert len(generated_list_voltages) == 20
    except ValueError as e:
        assert str(e) == "Voltage > 190."


def test_voltage_error():
    try:
        func_QC()
    except ValueError as e:
        assert str(e) == "Voltage > 190."
    else:
        raise AssertionError("Expected ValueError was not raised")








