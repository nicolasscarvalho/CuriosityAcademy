from funcs.func_QD import func_QD

def verify_dictionary(dictionary):
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
    for i in range(1, 11):
        generated_dict = func_QD()

        assert verify_dictionary(generated_dict) == True
