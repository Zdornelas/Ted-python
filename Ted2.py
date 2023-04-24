
vetor = [0] * 10


for i in range(10):
    numero = int(input("Digite um número: "))
    vetor[i] = numero


repetidos = []
for i in range(10):
    for j in range(i+1, 10):
        if vetor[i] == vetor[j]:
            if vetor[i] not in repetidos:
                repetidos.append(vetor[i])
            print("O número", vetor[i], "está nas posições", i, "e", j)

if len(repetidos) == 0:
    print("Não foram encontrados números repetidos no vetor.")
else:
    print("Os números repetidos foram encontrados nas seguintes posições:")
    for num in repetidos:
        posicoes = []
        for i in range(10):
            if vetor[i] == num:
                posicoes.append(i)
        print("Número", num, "nas posições", posicoes)