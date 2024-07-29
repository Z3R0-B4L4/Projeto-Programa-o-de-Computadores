opcao = 0
opt = 0

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
            p = int(input("Digite o número em decimal (0-9): "))
            print(f'{p} convertido para binário é {bin(p)[2:]}')
        elif opcao == 2:
            p = int(input("Digite o número em decimal (0-9): "))
            print(f'{p} convertido para hexadecimal é {hex(p)[2:]}')
        elif opcao == 3:
            p = int(input("Digite o número em decimal (0-9): "))
            print(f'{p} convertido para octal é {oct(p)[2:]}')
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
            p = input("Digite o número em binário (0-1): ")
            print(f'{p} convertido para decimal é {int(p, 2)}\n')
        elif opcao == 2:
            p = input("Digite o número em hexadecimal (0-9, A-F): ")
            print(f'{p} convertido para decimal é {int(p, 16)}')
        elif opcao == 3:
            p = input("Digite o número em octal (0-7): ")
            print(f'{p} convertido para decimal é {int(p, 8)}')
        elif opcao == 4:
            break
        else:
            print("Opção inválida\n")
    elif opt == 3:
        break
    else:
        print("Opção inválida!\n")
        print("""1. Converter decimal para outras bases.
2. Converter das bases Binário, Hexadecimal ou Octal para Decimal.
3. Sair""")