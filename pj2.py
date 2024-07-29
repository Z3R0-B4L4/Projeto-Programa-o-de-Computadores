opcao = 0
opt = 0

def dec_to_bin(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def dec_to_oct(decimal):
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def dec_to_hex(decimal):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ''
    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal

def bin_to_dec(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def oct_to_dec(octal):
    decimal = 0
    power = len(octal) - 1
    for digit in octal:
        decimal += int(digit) * (8 ** power)
        power -= 1
    return decimal

def hex_to_dec(hexadecimal):
    decimal = 0
    power = len(hexadecimal) - 1
    hex_chars = "0123456789ABCDEF"
    for digit in hexadecimal:
        decimal += hex_chars.index(digit.upper()) * (16 ** power)
        power -= 1
    return decimal

while True:
    print("Selecione uma opção:")
    print("""1. Converter decimal para outras bases.
2. Converter das bases Binário, Hexadecimal ou Octal para Decimal.
3. Sair""")
    opt = int(input())

    if opt == 1:
        print("Selecione uma opção de conversão do decimal para outras bases:")
        print("""1. Binário
2. Hexadecimal
3. Octal
4. Sair""")
        opcao = int(input())
        if opcao == 1:
            numero_decimal = int(input("Digite o número em decimal (0-9): "))
            numero_binario = dec_to_bin(numero_decimal)
            print(f'{numero_decimal} convertido para binário é {numero_binario}')
        elif opcao == 2:
            numero_decimal = int(input("Digite o número em decimal (0-9): "))
            numero_hexadecimal = dec_to_hex(numero_decimal)
            print(f'{numero_decimal} convertido para binário é {numero_hexadecimal}')
        elif opcao == 3:
            numero_decimal = int(input("Digite o número em decimal (0-9): "))
            numero_octal = dec_to_oct(numero_decimal)
            print(f'{numero_decimal} convertido para binário é {numero_octal}')
        elif opcao == 4:
            break
        else:
            print("Opção inválida\n")

    elif opt == 2:
        print("Selecione uma opção de conversão para decimal:")
        print("""1. Binário
2. Hexadecimal
3. Octal
4. Sair""")
        opcao = int(input())
        if opcao == 1:
            numero_binario = input("Digite o número em binario (0-1): ")
            print(f'{numero_binario} convertido para decimal é {bin_to_dec(numero_binario)}')
        elif opcao == 2:
            numero_hexadecimal = input("Digite o número em binario (0-1): ")
            print(f'{numero_hexadecimal} convertido para decimal é {hex_to_dec(numero_hexadecimal)}')
        elif opcao == 3:
            numero_octal = input("Digite o número em binario (0-1): ")
            print(f'{numero_octal} convertido para decimal é {oct_to_dec(numero_octal)}')
        elif opcao == 4:
            break
        else:
            print("Opção inválida\n")
    elif opt == 3:
        break
    else:
        print("Opção inválida!\n")
