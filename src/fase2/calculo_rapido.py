def somarInteiros(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

soma = int(input())
a = int(input())
b = int(input())

if 1 <= soma <= 36 and a <= b:
    if 1 <= a <= 10000 and 1 <= b <= 10000:
        d = 0
        e = []
        resposta = 0
        
        while d < b:
            if d==0:
                d+=a
                e.append(int(1))
                pass
            d += 1
            e.append(int(d))
        
        for d in e:
            if (somarInteiros(d) == soma):
                resposta+=1

print(resposta)
