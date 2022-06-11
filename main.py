from random import randint, choice


def generate_name() -> str:
    consonants: list[str] = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                             'x', 'y', 'z']

    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']

    with open("suffix.txt", 'r') as file:
        suffix: list[str] = [line.strip() for line in file]

    name_dict = {
        # COMBO OF 4
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

        # COMBO OF 3
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

        # COMBO OF 2
        25: "CC",
        26: "CV",
        27: "VC",
        28: "VV",
    }
    name_type = randint(1, len(name_dict))
    name_code = name_dict[name_type]

    name: str = ""

    consonants_sample = [choice(consonants) for _ in range(4)]
    vowels_sample = [choice(vowels) for _ in range(4)]
    consonants_index = 0
    vowels_index = 0

    for letter in name_code:
        if letter != " ":
            if letter == "C":
                name += consonants_sample[consonants_index]
                consonants_index += 1
            else:
                name += vowels_sample[vowels_index]
                vowels_index += 1

    return (name + choice(suffix)).capitalize()


if __name__ == "__main__":
    for _ in range(0, 10):
        print(generate_name())
