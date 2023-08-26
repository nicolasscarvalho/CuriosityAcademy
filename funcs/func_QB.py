def func_QB(temperature: int):
    """
    Checks if temperature is greater than 80 degrees.

    Raises:
        DANGEROUS temperature: If temperature > 80
    """

    if temperature > 80:
        ValueError("DANGEROUS temperature")
    else:
        return "OK Temperature"