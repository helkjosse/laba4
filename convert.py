# Числа от 1 до 9 (количественные числительные)
A_quant = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
# Числа от 1 до 9 (собирательные числительные)
A_col = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

# Числа от 11 до 19
B = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать",
     "восемнадцать", "девятнадцать"]

# Десятки (от 10 до 90)
C = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

# Сотые (от 100 до 900)
D = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

# Тысячи
thousands = ["тысяча", "тысячи", "тысяч"]

# Рубли
rubles = ["рубль", "рубля", "рублей"]


def convert_number_to_words(number: int) -> str:
    if number > 999999:
        return "Перевод чисел в слова не реализован для значений больше 999999"

    result = ""

    if 1000000 > number >= 1000:
        result += convert_thousands_to_words(number) + " "
        number %= 1000

    hundreds = number // 100
    tens = (number % 100) // 10
    ones = (number % 10)

    if hundreds > 0:
        result += D[hundreds - 1] + " "

    if tens > 0:
        if tens == 1 and ones > 0:
            result += B[ones - 1] + " " + rubles[2]
            return result
        else:
            result += C[tens - 1] + " "

    if ones > 0:
        if ones == 1:
            result += A_quant[ones - 1] + " " + rubles[0]
        elif 1 < ones < 5:
            result += A_quant[ones - 1] + " " + rubles[1]
        else:
            result += A_quant[ones - 1] + " " + rubles[2]
    if ones == 0:
        result += rubles[2]

    return result.capitalize()


def convert_thousands_to_words(number: int) -> str:
    result = ""

    if number > 99999:
        hundreds = number // 100000
        tens = (number % 100000) // 10000
        ones = (number % 10000) // 1000
    elif number > 9999:
        hundreds = 0
        tens = number // 10000
        ones = (number % 10000) // 1000
    else:
        hundreds = 0
        tens = 0
        ones = number // 1000

    if hundreds > 0:
        result += D[hundreds - 1] + " "

    if tens > 0:
        if tens == 1 and ones > 0:
            result += B[ones - 1] + " " + thousands[2]
            return result
        else:
            result += C[tens - 1] + " "

    if ones > 0:
        if ones == 1:
            result += A_col[ones - 1] + " " + thousands[0]
        elif 1 < ones < 5:
            result += A_col[ones - 1] + " " + thousands[1]
        else:
            result += A_col[ones - 1] + " " + thousands[2]
    if ones == 0:
        result += thousands[2]

    return result


if __name__ == "__main__":
    number1 = 1

    hundreds1 = number1 // 100
    tens1 = (number1 % 100) // 10
    ones1 = (number1 % 10)

    print(hundreds1, tens1, ones1)

    print(convert_number_to_words(56000))
    print(convert_number_to_words(156000))
    print(convert_number_to_words(6000))

    print(convert_number_to_words(100000))
    print(convert_number_to_words(114000))
    print(convert_number_to_words(1000))

    print(convert_number_to_words(100))
    print(convert_number_to_words(114))
    print(convert_number_to_words(1))
