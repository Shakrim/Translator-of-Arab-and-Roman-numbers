def to_roman(arab_num: int) -> str:
    result = ""
    translator = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                 900: "CM", 1000: "M"}

    # assignment the value of the highest key into the variable
    for arab in sorted(translator, reverse=True):
        # variable arab provides key to the value saved in variable roman
        roman = translator[arab]
        result += arab_num // arab * roman
        arab_num %= arab
    return result

rimske_cislo = to_roman(144)
print(rimske_cislo)

def to_arab(roman):
    mapping1 = {'IV':4, 'IX': 9,'XL':40, 'XC':90, 'CD':400, 'CM':900}
    mapping2 = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
    result = 0
    #Číslo roman postupně zmenšujeme, nakonec zbyde prázdný string
    while roman:
        if roman[:2] in mapping1:
            num = roman[:2]
            roman=roman[2:]
            mapping = mapping1
        else:
            num = roman[:1]
            roman = roman[1:]
            mapping = mapping2

        result += mapping[num]

    return result

arabske_cislo = to_arab('MMMCMXCIX')
print(arabske_cislo)


