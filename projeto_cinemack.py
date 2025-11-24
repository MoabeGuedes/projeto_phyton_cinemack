#Projeto 2 (Guilherme Gomes Pinho - Moabe da Silva Guedes Rêgo - Ryan Silva de Sousa)

# Inicialização das variáveis globais
# Listas para armazenar os tipos de ingressos vendidos por sessão
f1s1 = []
f1s2 = []
f2s1 = []
f2s2 = []
f3s1 = []
f3s2 = []

# Contadores de assentos disponíveis por sessão
contf1s1 = [0]*50
contf1s2 = [0]*50
contf2s1 = [0]*40
contf2s2 = [0]*40
contf3s1 = [0]*30
contf3s2 = [0]*30

# Listas para armazenar os valores dos ingressos vendidos por sessão
ingf1s1 = []
ingf1s2 = []
ingf2s1 = []
ingf2s2 = []
ingf3s1 = []
ingf3s2 = []

# Listas para armazenar as avaliações dos filmes
notas1 = []
notas2 = []
notas3 = []

critica_list1 = []
critica_list2 = []
critica_list3 = []

# Função de entrada do sistema, com menu principal e validação de opções
def entrada():
    print("\n\nBem vindo ao CineMack! Qual é o seu plano para hoje?")
    print("====================================================")
    print("1. Comprar ingressos para De Volta para o Futuro - Sessão 1\n2. Comprar ingressos para De Volta para o Futuro - Sessão 2\n3. Comprar ingressos para Interestelar - Sessão 1\n4. Comprar ingressos para Interestelar - Sessão 2\n5. Comprar ingressos para Clube da Luta - Sessão 1\n6. Comprar ingressos para Clube da Luta - Sessão 2\n7. Avaliar um filme\n8. Encerrar o dia e exibir o relatório")
    print("====================================================")
    op = int(input("Escolha a opção desejada: "))
    while op <=0 or op >= 9:
        op = int(input("Opção inválida, escolha a opção desejada (1-8): "))
    return op
    
# Função para avaliação dos filmes com validação de entradas
def avaliacao_filme():
    print("Obrigado por assistir o filme conosco!\nPara avaliar o filme que voce assistiu, escolha uma das opções abaixo:")
    print("====================================================")
    print("1. De Volta para o Futuro\n2. Interestelar\n3. Clube da Luta")
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
        op = input("Deseja adicionar uma crítica ao filme? s/n -- ").lower()
        #validacao
        while op != "s" and op != "n":
            op = input("Resposta inválida! digite somente s/n -- ").lower()
        if op == "n":
            critica_list1.append("S/A")
        if op == "s":
            critica(filme)
    elif filme == 2:
        notas2.append(nota)
        op = input("Deseja adicionar uma crítica ao filme? s/n -- ").lower()
        #validacao
        while op != "s" and op != "n":
            op = input("Resposta inválida! digite somente s/n -- ").lower()
        if op == "n":
            critica_list2.append("S/A")
        if op == "s":
            critica(filme)
    elif filme == 3:
        notas3.append(nota)
        op = input("Deseja adicionar uma crítica ao filme? s/n -- ").lower()
        #validacao
        while op != "s" and op != "n":
            op = input("Resposta inválida! digite somente s/n -- ").lower()
        if op == "n":
            critica_list3.append("S/A")
        if op == "s":
            critica(filme)
    print(f"Obrigado por avaliar o filme! Sua nota de {nota} foi registrada com sucesso.")

# Função para compra de ingressos por sessão, com controle de assentos, confirmação de compra e opção de voltar ao menu principal
def compraring(op):
    if op == 1: #Filme 1 - Sessão 1
        global contf1s1
        tempf1s1 = 0
        tempocupado = []
        print("\n\nDe Volta para o Futuro - Sessão 1\n====================================================")
        print(f"Assentos disponíveis: {contf1s1.count(0)}")
        for i in range(len(contf1s1)):
            if contf1s1[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$20\n2. Meia: R$10\n3. VIP: R$30\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf1s1)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s1[lugar] == 1 or lugar < 0 or lugar > 50:
                    print("Desculpe, assento inválido ou ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s1.append(20)
                    f1s1.append("int")
                    contf1s1[lugar] = 1
                    tempf1s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s1[lugar] == 1 or lugar < 0 or lugar > 50:
                    print("Desculpe, assento inválido ou ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s1.append(10)
                    f1s1.append("meia")
                    contf1s1[lugar] = 1
                tempf1s1 += 1
                tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s1[lugar] == 1 or lugar < 0 or lugar > 50:
                    print("Desculpe, assento inválido ou ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s1.append(30)
                    f1s1.append("vip")
                    contf1s1[lugar] = 1
                    tempf1s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf1s1}\nValor da compra: R${sum(ingf1s1[-tempf1s1:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf1s1[j] = 0
                if tempf1s1 > 0:
                    del ingf1s1[-tempf1s1:]
                    del f1s1[-tempf1s1:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
        
    elif op == 2: #Filme 1 - Sessão 2
        global contf1s2
        tempf1s2 = 0
        tempocupado = []
        print("\n\nDe Volta para o Futuro - Sessão 2\n====================================================")
        print(f"Assentos disponíveis: {contf1s2.count(0)}")
        for i in range(len(contf1s2)):
            if contf1s2[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$20\n2. Meia: R$10\n3. VIP: R$30\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf1s2)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while lugar < 0 or lugar > 50:
                        print("Assento inválido. Por favor, escolha um assento entre 0 e 50.")
                        lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                    while lugar < 0 or lugar > 50:
                        print("Assento inválido. Por favor, escolha um assento entre 0 e 50.")
                        lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s2.append(20)
                    f1s2.append("int")
                    contf1s2[lugar] = 1
                    tempf1s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s2.append(10)
                    f1s2.append("meia")
                    contf1s2[lugar] = 1
                    tempf1s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-50): "))
                while contf1s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-50): "))
                else:
                    ingf1s2.append(30)
                    f1s2.append("vip")
                    contf1s2[lugar] = 1
                    tempf1s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf1s2}\nValor da compra: R${sum(ingf1s2[-tempf1s2:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf1s2[j] = 0
                if tempf1s2 > 0:
                    del ingf1s2[-tempf1s2:]
                    del f1s2[-tempf1s2:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 3: #Filme 2 - Sessão 1
        global contf2s1
        tempf2s1 = 0
        tempocupado = []
        print("\n\nInterestelar - Sessão 1\n====================================================")
        print(f"Assentos disponíveis: {contf2s1.count(0)}")
        for i in range(len(contf2s1)):
            if contf2s1[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$15\n2. Meia: R$7.5\n3. VIP: R$22.5\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf2s1)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s1.append(15)
                    f2s1.append("int")
                    contf2s1[lugar] = 1
                    tempf2s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s1.append(7.5)
                    f2s1.append("meia")
                    contf2s1[lugar] = 1
                    tempf2s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s1.append(22.5)
                    f2s1.append("vip")
                    contf2s1[lugar] = 1
                    tempf2s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf2s1}\nValor da compra: R${sum(ingf2s1[-tempf2s1:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf2s1[j] = 0
                if tempf2s1 > 0:
                    del ingf2s1[-tempf2s1:]
                    del f2s1[-tempf2s1:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 4: #Filme 2 - Sessão 2
        global contf2s2
        tempf2s2 = 0
        tempocupado = []
        print("\n\nInterestelar - Sessão 2\n====================================================")
        print(f"Assentos disponíveis: {contf2s2.count(0)}")
        for i in range(len(contf2s2)):
            if contf2s2[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$15\n2. Meia: R$7.5\n3. VIP: R$22.5\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf2s2)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s2.append(15)
                    f2s2.append("int")
                    contf2s2[lugar] = 1
                    tempf2s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s2.append(7.5)
                    f2s2.append("meia")
                    contf2s2[lugar] = 1
                    tempf2s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-40): "))
                while contf2s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-40): "))
                else:
                    ingf2s2.append(22.5)
                    f2s2.append("vip")
                    contf2s2[lugar] = 1
                    tempf2s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf2s2}\nValor da compra: R${sum(ingf2s2[-tempf2s2:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf2s2[j] = 0
                if tempf2s2 > 0:
                    del ingf2s2[-tempf2s2:]
                    del f2s2[-tempf2s2:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 5: #Filme 3 - Sessão 1
        global contf3s1
        tempf3s1 = 0
        tempocupado = []
        print("\n\nClube da Luta - Sessão 1\n====================================================")
        print(f"Assentos disponíveis: {contf3s1.count(0)}")
        for i in range(len(contf3s1)):
            if contf3s1[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$10\n2. Meia: R$5\n3. VIP: R$15\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf3s1)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s1.append(10)
                    f3s1.append("int")
                    contf3s1[lugar] = 1
                    tempf3s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s1.append(5)
                    f3s1.append("meia")
                    contf3s1[lugar] = 1
                    tempf3s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s1[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s1.append(15)
                    f3s1.append("vip")
                    contf3s1[lugar] = 1
                    tempf3s1 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf3s1}\nValor da compra: R${sum(ingf3s1[-tempf3s1:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf3s1[j] = 0
                if tempf3s1 > 0:
                    del ingf3s1[-tempf3s1:]
                    del f3s1[-tempf3s1:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 6: #Filme 3 - Sessão 2
        global contf3s2
        tempf3s2 = 0
        tempocupado = []
        print("\n\nClube da Luta - Sessão 2\n====================================================")
        print(f"Assentos disponíveis: {contf3s2.count(0)}")
        for i in range(len(contf3s2)):
            if contf3s2[i] == 0:
                print(f"[{i}]", end=" ")
            else:
                print("[X]", end=" ")
        print("\n\nEscolha o seu ingresso!(Um por vez)\n1. Inteira: R$10\n2. Meia: R$5\n3. VIP: R$15\n4. Confirmar compra\n5. Voltar")
        print("====================================================")
        for i in range(len(contf3s2)):
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s2.append(10)
                    f3s2.append("int")
                    contf3s2[lugar] = 1
                    tempf3s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 2:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s2.append(5)
                    f3s2.append("meia")
                    contf3s2[lugar] = 1
                    tempf3s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 3:
                lugar = int(input(f"Escolha o seu assento (0-30): "))
                while contf3s2[lugar] == 1:
                    print("Desculpe, este assento já está ocupado. Por favor, escolha outro assento.")
                    lugar = int(input(f"Escolha o seu assento (0-30): "))
                else:
                    ingf3s2.append(15)
                    f3s2.append("vip")
                    contf3s2[lugar] = 1
                    tempf3s2 += 1
                    tempocupado.append(lugar)
            elif tipoing == 4:
                print("====================================================")
                print(f"Obrigado por comprar no CineMack!\nTotal de ingressos comprados: {tempf3s2}\nValor da compra: R${sum(ingf3s2[-tempf3s2:])}")
                print("====================================================")
                break
            elif tipoing == 5:
                for j in tempocupado:
                    contf3s2[j] = 0
                if tempf3s2 > 0:
                    del ingf3s2[-tempf3s2:]
                    del f3s2[-tempf3s2:]
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 7: #Avaliação
        avaliacao_filme()

# Função para gerar o relatório diário com vendas e avaliações, detalhado por filme e sessão 
def relatorio():
    print("\n\n\n\n\n\n-------------------------------------RELATORIO DIÁRIO-------------------------------------")
    cont = 1
    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0
    print(f"\n\nDe Volta para o Futuro - Sessão 1")
    print("===================================")
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
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"\n\n\n\nDe Volta para o Futuro - Sessão 2")
    print("===================================")
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
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")
   
    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0
    
    print(f"\n\n\n\nInterestelar - Sessão 1")
    print("===================================")
    for j in range(len(f2s1)):
        if f2s1[j] == "int":
            quant_int += 1
            valor_int += 15
        elif f2s1[j] == "meia":
            quant_meia += 1
            valor_meia += 7.5
        elif f2s1[j] == "vip":
            quant_vip += 1
            valor_vip += 22.5    
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"\n\n\n\nInterestelar - Sessão 2")
    print("===================================")
    for j in range(len(f2s2)):
        if f2s2[j] == "int":
            quant_int += 1
            valor_int += 15
        elif f2s2[j] == "meia":
            quant_meia += 1
            valor_meia += 7.5
        elif f2s2[j] == "vip":
            quant_vip += 1
            valor_vip += 22.5
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"\n\n\n\nClube da Luta - Sessão 1")
    print("===================================")
    for j in range(len(f3s1)):
        if f3s1[j] == "int":
            quant_int += 1
            valor_int += 10
        elif f3s1[j] == "meia":
            quant_meia += 1
            valor_meia += 5
        elif f3s1[j] == "vip":
            quant_vip += 1
            valor_vip += 15    
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")

    quant_int = quant_meia = quant_vip = 0
    valor_int = valor_meia = valor_vip = 0

    print(f"\n\n\n\nClube da Luta - Sessão 2")
    print("===================================")
    for j in range(len(f3s2)):
        if f3s2[j] == "int":
            quant_int += 1
            valor_int += 10
        elif f3s2[j] == "meia":
            quant_meia += 1
            valor_meia += 5
        elif f3s2[j] == "vip":
            quant_vip += 1
            valor_vip += 15
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira - {quant_int}\nMeia - {quant_meia}\nVIP - {quant_vip}\n")
    print(f"Receita:")
    print(f"Inteira - R${valor_int}\nMeia - R${valor_meia}\nVIP - R${valor_vip}")
    print("===================================")
        
    print("\n\n\n\n===========TOTAL DO DIA===========")
    total_ingressos = (len(f1s1) + len(f1s2) + len(f2s1) + len(f2s2) + len(f3s1) + len(f3s2))
    print(f"Total de ingressos vendidos: {total_ingressos}")
    receita_total = sum(ingf1s1) + sum(ingf1s2) + sum(ingf2s1) + sum(ingf2s2) + sum(ingf3s1) + sum(ingf3s2)
    print(f"Receita total: R${receita_total}")
    print("==================================")

    
    print(f"\n\n\n\nMÉDIA DAS AVALIAÇÕES DOS FILMES")
    print("===================================")
    media1 = media2 = media3 = 0
    for j in range(len(notas1)):
        media1 = sum(notas1) / len(notas1)
    print(f"De Volta para o Futuro: {media1:.1f}")
    for j in range(len(notas2)):
        media2 = sum(notas2) / len(notas2) 
    print(f"Interestelar: {media2:.1f}")
    for j in range(len(notas3)):
        media3 = sum(notas3) / len(notas3) 
    print(f"Clube da Luta: {media3:.1f}") 
    print("===================================")
    print(f"\nLista de Críticas sobre o De Volta para o futuro:")
    for j in range(len(critica_list1)):
        if critica_list1[j] != "S/A": 
            print(f"\n- {critica_list1[j]}\n\n")
    print(f"Lista de Críticas sobre o Interestelar:")
    for j in range(len(critica_list2)):
        if critica_list2[j] != "S/A": 
            print(f"\n- {critica_list2[j]}\n\n")
            
    print(f"Lista de Críticas sobre o Clube da Luta:")
    for j in range(len(critica_list3)):
        if critica_list3[j] != "S/A": 
            print(f"\n- {critica_list3[j]}\n\n")


def critica(filme):
    if filme == 1:
        critica_list1.append(input("Informe sua resenha: "))
        for i in range(len(critica_list1)):
            while critica_list1[i] == "":
                critica_list1[i] = input("Resenha vazia! Digite novamente: \n")
    elif filme == 2:
        critica_list2.append(input("Informe sua resenha: "))
        for i in range(len(critica_list2)):
            while critica_list2[i] == "":
                critica_list2[i] = input("Resenha vazia! Digite novamente: \n")
    else:
        critica_list3.append(input("Informe sua resenha: "))
        for i in range(len(critica_list3)):
            while critica_list3[i] == "":
                critica_list3[i] = input("Resenha vazia! Digite novamente: \n")
# Função principal
def main():
    while True: 
        op = entrada()
        if op == 8:
            relatorio()
            break
        compraring(op)


main()