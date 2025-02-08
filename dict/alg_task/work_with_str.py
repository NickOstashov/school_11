# задача: дана произвольная строка, нужно вывести все символы в отсоритированном порядке

def solution_1(input_str: str) -> str:
    dict_by_symbol = dict()
    for symbol in input_str:
        if not symbol in dict_by_symbol:
            dict_by_symbol[symbol] = 0

        dict_by_symbol[symbol] += 1

    sorted_keys = sorted(dict_by_symbol.keys())
    res = ''
    for key in sorted_keys:
        res += key * dict_by_symbol[key]

    return res

def main():
    input_str = "abacaba"
    res_str = solution_1(input_str)
    print(res_str)

if __name__ == "__main__":
    main()


