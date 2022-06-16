from random import randint, choice


def generate_name() -> str:
    """
    Generate a random prefix and combine with a random suffix.

    Returns
    -------
    name : str
        The randomly generated name.

    """
    consonants: list[str] = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                             'x', 'y', 'z']

    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

    # construct a list from the file of suffixes
    with open("Assets/suffix.txt", 'r') as file:
        suffix: list[str] = [line.strip() for line in file]

    # name prefix combination codes
    # C stands for a consonant
    # V stands for a vowel
    # spaces in the value are only to improve readability
    name_dict = {
        # 4 LETTER COMBO
        # CC start
        1: "CC CC",
        2: "CC CV",
        3: "CC VC",
        4: "CC VV",
        # CV start
        5: "CV CC",
        6: "CV CV",
        7: "CV VC",
        8: "CV VV",
        # VC start
        9: "VC CC",
        10: "VC CV",
        11: "VC VC",
        12: "VC VV",
        # VV start
        13: "VV CC",
        14: "VV CV",
        15: "VV VC",
        16: "VV VV",

        # 3 LETTER COMBO
        # C start
        17: "C CC",
        18: "C CV",
        19: "C VC",
        20: "C VV",
        # V start
        21: "V CC",
        22: "V CV",
        23: "V VC",
        24: "V VV",

        # 2 LETTER COMBO
        25: "CC",
        26: "CV",
        27: "VC",
        28: "VV",
    }

    # generate a random prefix key
    name_type = randint(1, len(name_dict))
    # get the value of the random key
    name_code = name_dict[name_type]

    prefix: str = ""

    # get a samples of 4 consonants and 4 vowels
    # any given name code will not be longer than 4 of one letter type
    consonants_sample = [choice(consonants) for _ in range(4)]
    vowels_sample = [choice(vowels) for _ in range(4)]

    # use to count how many consonants or vowels have been used
    consonants_index = 0
    vowels_index = 0

    # parse through the name code
    # and generate the prefix
    for letter in name_code:
        # if the current letter is not a space
        # determine if we need a consonant or a vowel
        if letter != " ":
            # if the current letter is a C
            # append a consonant to the prefix
            # and increase the consonants used count
            if letter == "C":
                prefix += consonants_sample[consonants_index]
                consonants_index += 1

            # the current letter will be a V
            # append a vowel to the prefix
            # and increase the vowels used count
            else:
                prefix += vowels_sample[vowels_index]
                vowels_index += 1

    # construct a name combining the prefix with a random suffix
    # and capitalize
    name = (prefix + choice(suffix)).capitalize()

    return name
