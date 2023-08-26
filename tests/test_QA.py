from funcs.func_QA import func_QA

def verify_list_type(list_data: list):
    """
    Verify the type of the list

    returns:
        True: if the list is purely composed of integers
        False: if the list is not purely composed of integers
    """
    for element in list_data:
        if type(element) != int:
            return False
    
    return True

def test_QA():
    """
    Tests if the list size is 20 items and then checks if it is purely integers
    """
    for i in range(1, 11):
        
        generate_list = func_QA()

        assert len(generate_list) == 20
        assert verify_list_type(generate_list) == True