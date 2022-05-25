def convert(rnum):
    roman_keys = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000, 'IV': 4, 'IX': 9,
        'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    total = 0
    ind = 0

    while ind < len(rnum):  # while our moving index is less than length of the roman numeral

        if ind + 1 < len(rnum) and rnum[ind:ind + 2] in roman_keys:
            # If we have characters left in the rnum arg, if the substring exists within our keys dict

            total += roman_keys[rnum[ind:ind + 2]]
            # Total = the value of the key at the matching space/index

            ind += 2
            # we increment by 2 here since we counted 2 numerals

        else:
            # inside the else, we are just counting and adding a single roman numeral rathern than 2

            total += roman_keys[rnum[ind]]

            ind += 1

    return total
