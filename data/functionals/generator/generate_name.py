from random import choice

from data.functionals.generator.prefix_code_gen import prefix_code_gen


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
    with open("data/assets/suffix.txt", 'r') as file:
        suffix: list[str] = [line.strip() for line in file]

    # generate list of name prefix combination codes
    # function returns a list of name codes
    # from length 2 to 5 consisting of C and V
    # C stands for a consonant
    # V stands for a vowel
    name_codes = prefix_code_gen()

    # generate a random name code
    name_code = choice(name_codes)

    prefix: str = ""

    # get a samples of 5 consonants and 5 vowels
    # any given name code will not be longer than 5 of one letter type
    consonants_sample = [choice(consonants) for _ in range(5)]
    vowels_sample = [choice(vowels) for _ in range(5)]

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
