#from funcs.func_QE import func_QE
from func_QE import func_QE

def test_length_of_currents(list_of_currents: list[int]) -> bool:
    """
        Checks if the int list has exactly 30 items
        
        This procedures checks if the int list returned by
        test_QE function has 30 items.
    """
    
    if len(list_of_currents) != 30:
        return False
    return True
    
def test_if_current_is_on_range(list_of_currents: list[int]) -> bool:
    """
    Checks if each element of the list is on the range: ]25mA, 800mA[
        
    """
    
    for cur in list_of_currents:
        if cur > 800 or cur < 25:
            return False
    return True
        
def test_if_is_only_integer(list_of_currents: list[int]) -> bool:
    """
    Tests if the given list has only int type elements
    """
    
    for cur in list_of_currents:
        if type(cur) != int:
            return False
    return True

def test_func_QE() -> None:
    generated_list_of_currents = func_QE()
    
    assert test_if_is_only_integer(generated_list_of_currents)
    assert test_length_of_currents(generated_list_of_currents)
    assert test_if_current_is_on_range(generated_list_of_currents)
        