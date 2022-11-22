# potentially will use this stuff as a common lib or just copy stuff

def parse_input_into_list_of_strings(input_file: str) -> list:
    input_list = []

    f = open(input_file, "r")

    for line in f:
        input_list.append(line)

    f.close()

    return input_list


def parse_input_into_list_of_ints(input_file: str) -> list:
    input_list = []

    f = open(input_file, "r")

    for line in f:
        input_list.append(int(line))

    f.close()

    return input_list