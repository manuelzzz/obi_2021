alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vogais = ["a", "e", "i", "o", "u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

# a - 1 / e - 5 / i - 9 / 0 - 15 / u - 22

p = str(input())
resposta = ""

for letra in p:
    if letra in vogais:
        resposta+=letra
    if letra in consoantes:
        resposta+=letra
        for posicaoAlfabeto in range(0, len(alfabeto)):
            if alfabeto[posicaoAlfabeto] == letra:
                if posicaoAlfabeto <= 3:
                    resposta+="a"
                elif posicaoAlfabeto <= 7:
                    resposta+="e"
                elif posicaoAlfabeto <= 12:
                    resposta+="i"
                elif posicaoAlfabeto <= 18:
                    resposta+="o"
                else:
                    resposta+="u"
                    
        for posicaoConsoante in range(0, len(consoantes)):
            if letra == consoantes[posicaoConsoante]:
                if posicaoConsoante < len(consoantes):
                    resposta+=consoantes[posicaoConsoante + 1]
                else:
                    resposta+=consoantes[posicaoConsoante]

print(resposta)