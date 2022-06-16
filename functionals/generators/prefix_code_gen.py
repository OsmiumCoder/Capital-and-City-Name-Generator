from itertools import product


def prefix_code_gen() -> list[str]:
    """
    Generate a list of prefix codes.

    Returns
    -------
    prefix_codes : list[str]
        A list of string prefix codes.

    """
    prefix_codes = []

    # first loop determines length of prefix code
    # going from length 2 to length 5
    for i in range(2, 6):
        # loop through all the prefix codes of the current length
        # joining each tuple
        for j in product(["C", "V"], repeat=i):
            # join the values of the tuple
            name_code = "".join(j)
            # append each prefix code to the return list
            prefix_codes.append(name_code)

    return prefix_codes
