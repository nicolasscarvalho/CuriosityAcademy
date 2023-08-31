from funcs.func_QD import func_QD

def verify_dictionary(dictionary):
    """
    Verify if a dictionary meets the specified requirements.

    Args:
        dictionary (dict): The dictionary to be verified.

    Returns:
        bool: True if the dictionary meets the requirements, False otherwise.
    """
    verify_dictionary_requirements = {
        "temperature": {"count": 20, "type": int},
        "voltage": {"count": 20, "type": int},
        "current": {"count": 20, "type": int},
        "status": {"count": 5, "type": int},
        "type": {"count": 5, "type": str},
    }

    for key, reqs in verify_dictionary_requirements.items():
        if key not in dictionary or len(dictionary[key]) != reqs["count"]:
            return False

        if not all(isinstance(value, reqs["type"]) for value in dictionary[key]):
            return False

    return True

def test_QD():
    """
    Test the func_QD function by generating dictionaries and verifying them.

    For each dictionary generated by func_QD, verify if it meets the requirements using the verify_dictionary function.
    Use an assertion to check the verification success.
    """
    for i in range(1, 11):
        generated_dict = func_QD()

        assert verify_dictionary(generated_dict) == True
