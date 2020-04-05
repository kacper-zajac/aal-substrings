from collections import defaultdict


def calc_offset(z, y):
    if z > y:
        return z - y - 1
    return 0


def use(data, mode):
    amountof_mistakes = int(data[0])  # ile bledow moze byc w podciagu
    string1 = data[1]  # pierwszy ciag
    string2 = data[2]  # drugi ciag
    length1 = len(string1)
    length2 = len(string2)

    complexity = length2 + (length1) * (length1) * (2 + max(1, amountof_mistakes)) / (26 * 2)

    letters_map = defaultdict(list)

    iterator_map = 0
    while iterator_map < len(string2):
        letters_map[string2[iterator_map]].append(iterator_map)
        iterator_map += 1

    iterator_string1 = 0
    strings = []
    max_length = 0

    while iterator_string1 < (length1 - calc_offset(max_length, amountof_mistakes)):
        substrings = []
        iterator_map = 0

        while iterator_map < len(letters_map[string1[iterator_string1]]):
            iterator_string2 = letters_map[string1[iterator_string1]][iterator_map]
            if iterator_string2 > (length2 - calc_offset(max_length, amountof_mistakes)):
                iterator_map += 1
                continue

            if iterator_string1 > 0 and iterator_string2 > 0:
                if string1[iterator_string1 - 1] == string2[iterator_string2 - 1]:
                    iterator_map += 1
                    continue

            iterator_mistakes = 0
            iterator_string2_inner = iterator_string2 + 1
            iterator_string1_inner = iterator_string1 + 1
            new_string = [string1[iterator_string1], string2[iterator_string2]]
            while iterator_string2_inner < length2 and iterator_string1_inner < length1:
                if string1[iterator_string1_inner] != string2[iterator_string2_inner]:
                    if iterator_mistakes < amountof_mistakes:
                        iterator_mistakes += 1
                    else:
                        break
                new_string[0] += string1[iterator_string1_inner]
                new_string[1] += string2[iterator_string2_inner]
                iterator_string2_inner += 1
                iterator_string1_inner += 1
            if iterator_string2_inner == length2 or iterator_string1_inner == length1:
                if iterator_mistakes < amountof_mistakes:
                    # jesli dojdzie do konca stringa, a zostanie jeszcze mozliwosc bledu, zawroci i doda literki
                    iterator_mistakes = amountof_mistakes - iterator_mistakes
                    iterator_string1_inner = iterator_string1 - 1
                    iterator_string2_inner = iterator_string2 - 1
                    while iterator_mistakes > 0 and iterator_string2_inner >= 0 and iterator_string1_inner >= 0:
                        new_string[0] = string1[iterator_string1_inner] + new_string[0]
                        new_string[1] = string2[iterator_string2_inner] + new_string[1]
                        iterator_string2_inner -= 1
                        iterator_string1_inner -= 1
                        iterator_mistakes -= 1
            if len(max(new_string)) > max_length:
                max_length = len(max(new_string, key=len))
                substrings.append(new_string[0])
                substrings.append(new_string[1])
            iterator_map += 1
        iterator_string1 += 1
        if substrings:
            if len(max(substrings, key=len)) < max_length:
                pass
            else:
                max_length = len(max(substrings, key=len))
            for st in substrings:
                if len(st) == max_length:
                    strings.append(st)
    longest_strings = []
    if strings:
        max_length = len(max(strings, key=len))
        for st in strings:
            if len(st) == max_length:
                longest_strings.append(st)
    if mode == 1:
        return complexity
    return longest_strings
