print("Введите список строк через пробел:", end=" ")
str_list = list(input().split(" "))
print("Ваш список строк:", end=" ")
print(str_list)

def coder(str_list):
    """
    Byte-coding your text
    str_list - list of your text
    """
    if  '' in str_list:
        print("Нужно что-нибудь вписать! В списке есть пустое значение!")
    else:
        print_codec = dict()

        for str_i in str_list:
            print_codec[str_i] = str_i.encode("utf-8")

        for key, value in print_codec.items():
            print("Строка: {0} байт-код: {1}".format(key, value))
    return print_codec

def decoder(code):
    """
    Uncoding your byte-code
    Code - your byte-code
    """
    if  '' in code:
        print("Нужно что-нибудь вписать! В списке есть пустое значение!")
    else:
        print_decodec = dict()

        for code_i in code:
            print_decodec[code_i] = code_i.decode("utf-8")

        for key, value in print_decodec.items():
            print("Байт-код: {0} строка: {1}".format(key, value))

usr_code = coder(str_list)
usr_code = list(usr_code.values())
decoder(usr_code)

