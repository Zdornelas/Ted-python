
vetor = [0] * 20


for i in range(20):
    numero = int(input("Digite um número: "))
    vetor[i] = numero


for i in range(19, -1, -1):
    print(vetor[i])