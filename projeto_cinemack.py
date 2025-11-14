#Projeto 2 (Guilherme Gomes Pinho - Moabe da Silva Guedes Rêgo - Ryan Silva de Sousa)
f1s1 = []
f1s2 = []
f2s1 = []
f2s2 = []
f3s1 = []
f3s2 = []

contf1s1 = 50
contf1s2 = 50
contf2s1 = 50
contf2s2 = 50
contf3s1 = 50
contf3s2 = 50

ingf1s1 = []
ingf1s2 = []
ingf2s1 = []
ingf2s2 = []
ingf3s1 = []
ingf3s2 = []

notas1 = []
notas2 = []
notas3 = []

def entrada():
    print("Menu Principal\n1. Comprar ingressos para Filme 1 - Sessão 1\n2. Comprar ingressos para Filme 1 - Sessão 2\n3. Comprar ingressos para Filme 2 - Sessão 1\n4. Comprar ingressos para Filme 2 - Sessão 2\n5. Comprar ingressos para Filme 3 - Sessão 1\n6. Comprar ingressos para Filme 3 - Sessão 2\n7. Avaliar um filme\n8. Encerrar o dia e exibir o relatório\n")
    op = int(input("Escolha a opção desejada: "))
    while op <=0 or op >= 9:
        op = int(input("Opção inválida, escolha a opção desejada (1-8): "))
    return op

def avaliacao_filme():
    print("Obrigado por assistir ao filme no CineMack!")
    filme = int(input("Por favor, digite o numero do filme que você assistiu: "))
    while filme < 1 or filme > 3:
        print("Filme inválido. Por favor, tente novamente.")
        filme = int(input("Por favor, digite o numero do filme que você assistiu: "))
    nota = int(input("Em uma escala de 0 a 10, como você avaliaria o filme? "))
    while nota < 0 or nota > 10:
        print("Nota inválida. Por favor, tente novamente.")
        nota = int(input("Em uma escala de 0 a 10, como você avaliaria o filme? "))
    if filme == 1:
        notas1.append(nota)
    elif filme == 2:
        notas2.append(nota)
    elif filme == 3:
        notas3.append(nota)
    print(f"Obrigado por avaliar o filme '{filme}' com a nota {nota}!")

def compraring(op):
    if op == 1: #Filme 1 - Sessão 1
        global contf1s1
        tempf1s1 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 1: {contf1s1}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf1s1.append(20)
                f1s1.append("int")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 2:
                ingf1s1.append(10)
                f1s1.append("meia")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 3:
                ingf1s1.append(30)
                f1s1.append("vip")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf1s1}")
                break
            elif tipoing == 5:
                contf1s1 += tempf1s1
                for i in range(tempf1s1 - 1, -1, -1):
                    del ingf1s1[-1]
                    del f1s1[-1]    
                return

            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 2: #Filme 1 - Sessão 2
        global contf1s2
        tempf1s2 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf1s2}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf1s2.append(20)
                f1s2.append("int")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 2:
                ingf1s2.append(10)
                f1s2.append("meia")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 3:
                ingf1s2.append(30)
                f1s2.append("vip")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf1s2}")
                break
            elif tipoing == 5:
                contf1s2 += tempf1s2
                for i in range(tempf1s2 - 1, -1, -1):
                    del ingf1s2[-1]
                    del f1s2[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 3: #Filme 2 - Sessão 1
        global contf2s1
        tempf2s1 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf2s1}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf2s1.append(20)
                f2s1.append("int")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 2:
                ingf2s1.append(10)
                f2s1.append("meia")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 3:
                ingf2s1.append(30)
                f2s1.append("vip")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf2s1}")
                break
            elif tipoing == 5:
                contf2s1 += tempf2s1
                for i in range(tempf2s1 - 1, -1, -1):
                    del ingf2s1[-1]
                    del f2s1[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 4: #Filme 2 - Sessão 2
        global contf2s2
        tempf2s2 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf2s2}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf2s2.append(20)
                f2s2.append("int")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 2:
                ingf2s2.append(10)
                f2s2.append("meia")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 3:
                ingf2s2.append(30)
                f2s2.append("vip")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf2s2}")
                break
            elif tipoing == 5:
                contf2s2 += tempf2s2
                for i in range(tempf2s2 - 1, -1, -1):
                    del ingf2s2[-1]
                    del f2s2[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 5: #Filme 3 - Sessão 1
        global contf3s1
        tempf3s1 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf3s1}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf3s1.append(20)
                f3s1.append("int")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 2:
                ingf3s1.append(10)
                f3s1.append("meia")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 3:
                ingf3s1.append(30)
                f3s1.append("vip")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf3s1}")
                break
            elif tipoing == 5:
                contf3s1 += tempf3s1
                for i in range(tempf3s1 - 1, -1, -1):
                    del ingf3s1[-1]
                    del f3s1[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 6: #Filme 3 - Sessão 2
        global contf3s2
        tempf3s2 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf3s2}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingf3s2.append(20)
                f3s2.append("int")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 2:
                ingf3s2.append(10)
                f3s2.append("meia")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 3:
                ingf3s2.append(30)
                f3s2.append("vip")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf3s2}")
                break
            elif tipoing == 5:
                contf3s2 += tempf3s2
                for i in range(tempf3s2 - 1, -1, -1):
                    del ingf3s2[-1]
                    del f3s2[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 7: #Avaliação
        avaliacao_filme()


def relatorio():
    print("-----RELATORIO FINAL-----")
    cont = 1
    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0
    print(f"Filme 1 - Sessão 1")
    for j in range(len(f1s1)):
        if f1s1[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f1s1[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f1s1[j] == "vip":
            quant_vip += 1
            valor_vip += 30
        
    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")
    
    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"Filme 1 - Sessão 2")
    for j in range(len(f1s2)):
        if f1s2[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f1s2[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f1s2[j] == "vip":
            quant_vip += 1
            valor_vip += 30

    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")
    
    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0
    
    print(f"Filme 2 - Sessão 1")
    for j in range(len(f2s1)):
        if f2s1[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f2s1[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f2s1[j] == "vip":
            quant_vip += 1
            valor_vip += 30
        
    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"Filme 2 - Sessão 2")
    for j in range(len(f2s2)):
        if f2s2[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f2s2[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f2s2[j] == "vip":
            quant_vip += 1
            valor_vip += 30

    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"Filme 3 - Sessão 1")
    for j in range(len(f3s1)):
        if f3s1[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f3s1[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f3s1[j] == "vip":
            quant_vip += 1
            valor_vip += 30
        
    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"Filme 3 - Sessão 2")
    for j in range(len(f3s2)):
        if f3s2[j] == "int":
            quant_int += 1
            valor_int += 20
        elif f3s2[j] == "meia":
            quant_meia += 1
            valor_meia += 10
        elif f3s2[j] == "vip":
            quant_vip += 1
            valor_vip += 30

    print("Quantidade de ingressos vendidos")
    print(f"INTEIRA - {quant_int}\nMEIA - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"RECEITA POR TIPO (Sessão {cont})")
    print(f"INTEIRA - {valor_int}\nMEIA - {valor_meia}\nVIP - {valor_vip}\n")

    media1 = media2 = media3 = 0
    for j in range(len(notas1)):
        media1 = sum(notas1) / len(notas1)
    print(f"Média de avaliações:\nFilme 1: {media1:.1f}")
    for j in range(len(notas2)):
        media2 = sum(notas2) / len(notas2) 
    print(f"Filme 2: {media2:.1f}")
    for j in range(len(notas3)):
        media3 = sum(notas3) / len(notas3) 
    print(f"Filme 3: {media3:.1f}")         

    total_ingressos = (len(f1s1) + len(f1s2) + len(f2s1) + len(f2s2) + len(f3s1) + len(f3s2))
    print(f"Total de ingressos vendidos no dia: {total_ingressos}")
    receita_total = sum(ingf1s1) + sum(ingf1s2) + sum(ingf2s1) + sum(ingf2s2) + sum(ingf3s1) + sum(ingf3s2)
    print(f"Receita total do dia: {receita_total}")

def main():
    while True: 
        op = entrada()
        if op == 8:
            relatorio()
            break
        compraring(op)


main()