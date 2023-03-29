def fatorial(n):
    result, count = 1,1

    while count <= n:
        result *= count
        count += 1

    n = result
    return n

def analise(n, p):
    np = n-p
    return fatorial(n) / fatorial(np)

nm = input()
n,m = nm.split(" ")

n,m = int(n), int(m)
naoPossiveis = []

for i in range(0, m):
    naoPossiveis.append(input())

possiveis = analise(n, 4) - len(naoPossiveis)

if (m==0):
    possiveis+=1

print(int(possiveis))
