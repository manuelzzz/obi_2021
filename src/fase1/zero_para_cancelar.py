n = int(input())
numeros = []
resposta = ""

for i in range(0, n):
    numeros.append(int(input()))

for num in numeros:
    if num != 0:
        resposta+=str(num)
    else:
        resposta = resposta[:-1]

if resposta == "":
    print(0)
else:
    print(resposta)