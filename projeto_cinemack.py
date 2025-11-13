#Guilherme Gomes Pinho - Moabe da Silva Guedes Rêgo - Ryan Silva de Sousa
f1s1 = []
contf1s1 = 50

f1s2 = []
f2s1 = []
f2s2 = []
f3s1 = []
f3s2 = []

def entrada():
    op = int(input("Escolha a opção desejada: "))
    while op <=0 or op >= 9:
        op = int(input("Opção inválida, escolha a opção desejada (1-8): "))
    return op


def compraring(op):
    if op == 1:
        global contf1s1
        ingressos = []
        print(f"Assentos disponíveis para Filme 1 - Sessão 1: {cont}\nEscolha o tipo de ingresso (1: Inteira, 2: Meia, 3: VIP, 4: Confirmar compra, 5: Voltar): ")
        tipoing = int(input(""))
        for i in range(cont):
            if tipoing == 1:
                ingressos[i].append(20)
                f1s1.append(int)


def main():
    print("Menu Principal\n1. Comprar ingressos para Filme 1 - Sessão 1\n2. Comprar ingressos para Filme 1 - Sessão 2\n3. Comprar ingressos para Filme 2 - Sessão 1\n4. Comprar ingressos para Filme 2 - Sessão 2\n5. Comprar ingressos para Filme 3 - Sessão 1\n6. Comprar ingressos para Filme 3 - Sessão 2\n7. Avaliar um filme\n8. Encerrar o dia e exibir o relatório")
    op = entrada()
