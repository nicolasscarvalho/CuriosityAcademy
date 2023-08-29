from funcs.func_QC import func_QC

def test_voltages_list():
    generated_list_voltages = func_QC()
    assert len(generated_list_voltages) == 20

