idades = []

idades.append(int(input()))
idades.append(int(input()))
idades.append(int(input()))

for index in range(1, len(idades)):
    valorAtual = idades[index]
    posicao = index
    
    while posicao > 0 and idades[posicao - 1] > valorAtual:
        idades[posicao] = idades[posicao-1]
        posicao = posicao - 1
    
    idades[posicao] = valorAtual

print(idades[1])