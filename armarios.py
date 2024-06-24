armarios = [0] * 10

def mostra_armarios():
    for i in range(10):
        if armarios[i] == 0:
            armario = 'Livre'
        else:
            armario = 'Ocupado'
        print(f"Armario {i}: {armario}")

def mostra_armarios_livres():
    livres = 0
    for i in range(10):
        if armarios[i] == 0:
            print(f"Armário {i}: Livre")
            livres += 1
    if livres == 0:
        print("Não temos armários disponíveis no momento.")

def utilizar_armario():
    numero = int(input("Informe o número do armário a ser utilizado: "))
    if numero < 0 or numero >= len(armarios):
        print("Número de armário inválido.")
    elif armarios[numero] == 0:
        armarios[numero] = 1
        print(f"Armário {numero} agora está Ocupado.")
    else:
        print("Armário já está sendo utilizado.")

def remover_armario():
    numero = int(input("Informe o número do armário a ser liberado: "))
    if numero < 0 or numero >= len(armarios):
        print("Esse armário não existe!")
    elif armarios[numero] == 1:
        armarios[numero] = 0
        print(f"Armário {numero} agora está Livre.")
    else:
        print("Esse armário já está livre.")

def resumo():
    livres = 0
    ocupados = 0
    for i in armarios:
        if i == 0:
            livres += 1
        else:
            ocupados += 1
    print(f"Armarios Livre: {livres}\nArmarios Ocupados: {ocupados}")

def menu():
    while True:
        print("Bem Vindo - Portal de Seleção de Armários Unoesc")
        print(f"1 - Mostrar Armários")
        print(f"2 - Mostrar Armários Livres")
        print(f"3 - Utilizar um Armário")
        print(f"4 - Remover um Armário")
        print(f"5 - Resumo")
        print(f"0 - Sair")

        select = int(input("Informe o número do que você deseja: "))
        if select == 1:
            mostra_armarios()
        elif select == 2:
            mostra_armarios_livres()
        elif select == 3:
            utilizar_armario()
        elif select == 4:
            remover_armario()
        elif select == 5:
            resumo()
        elif select == 0:
            print("Saindo do Sistema...")
            break
        else:
            print("Caracter invalido, ou inexistente")
menu()
