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

ingressos = []


def entrada():
    print("Menu Principal\n1. Comprar ingressos para Filme 1 - Sessão 1\n2. Comprar ingressos para Filme 1 - Sessão 2\n3. Comprar ingressos para Filme 2 - Sessão 1\n4. Comprar ingressos para Filme 2 - Sessão 2\n5. Comprar ingressos para Filme 3 - Sessão 1\n6. Comprar ingressos para Filme 3 - Sessão 2\n7. Avaliar um filme\n8. Encerrar o dia e exibir o relatório\n")
    op = int(input("Escolha a opção desejada: "))
    while op <=0 or op >= 9:
        op = int(input("Opção inválida, escolha a opção desejada (1-8): "))
    return op


def compraring(op):
    if op == 1: #Filme 1 - Sessão 1
        global contf1s1
        tempf1s1 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 1: {contf1s1}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingressos.append(20)
                f1s1.append("int")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f1s1.append("meia")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f1s1.append("vip")
                contf1s1 -= 1
                tempf1s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf1s1}")
                break
            elif tipoing == 5:
                contf1s1 += tempf1s1
                for i in range(tempf1s1 - 1, -1, -1):
                    del ingressos[-1]
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
                ingressos.append(20)
                f1s2.append("int")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f1s2.append("meia")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f1s2.append("vip")
                contf1s2 -= 1
                tempf1s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf1s2}")
                break
            elif tipoing == 5:
                contf1s2 += tempf1s2
                for i in range(tempf1s2 - 1, -1, -1):
                    del ingressos[-1]
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
                ingressos.append(20)
                f2s1.append("int")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f2s1.append("meia")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f2s1.append("vip")
                contf2s1 -= 1
                tempf2s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf2s1}")
                break
            elif tipoing == 5:
                contf2s1 += tempf2s1
                for i in range(tempf2s1 - 1, -1, -1):
                    del ingressos[-1]
                    del f2s1[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 3: #Filme 2 - Sessão 2
        global contf2s2
        tempf2s2 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf2s2}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingressos.append(20)
                f2s2.append("int")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f2s2.append("meia")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f2s2.append("vip")
                contf2s2 -= 1
                tempf2s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf2s2}")
                break
            elif tipoing == 5:
                contf2s2 += tempf2s2
                for i in range(tempf2s2 - 1, -1, -1):
                    del ingressos[-1]
                    del f2s2[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 3: #Filme 3 - Sessão 1
        global contf3s1
        tempf3s1 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf3s1}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingressos.append(20)
                f3s1.append("int")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f3s1.append("meia")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f3s1.append("vip")
                contf3s1 -= 1
                tempf3s1 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf3s1}")
                break
            elif tipoing == 5:
                contf3s1 += tempf3s1
                for i in range(tempf3s1 - 1, -1, -1):
                    del ingressos[-1]
                    del f3s1[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
    elif op == 3: #Filme 3 - Sessão 2
        global contf3s2
        tempf3s2 = 0
        print(f"Assentos disponíveis para Filme 1 - Sessão 2: {contf3s2}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        while True:
            tipoing = int(input("Escolha o ingresso: "))
            if tipoing == 1:
                ingressos.append(20)
                f3s2.append("int")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 2:
                ingressos.append(10)
                f3s2.append("meia")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 3:
                ingressos.append(30)
                f3s2.append("vip")
                contf3s2 -= 1
                tempf3s2 += 1
            elif tipoing == 4:
                print(f"Compra confirmada. Total de ingressos comprados: {tempf3s2}")
                break
            elif tipoing == 5:
                contf3s2 += tempf3s2
                for i in range(tempf3s2 - 1, -1, -1):
                    del ingressos[-1]
                    del f3s2[-1]    
                return
            else:
                print("Opção inválida, por favor escolha novamente.")
def main():
    while True: 
        op = entrada()
        if op == 8:
            print("relatório...")
            break
        compraring(op)
        print(ingressos, f1s1)

main()