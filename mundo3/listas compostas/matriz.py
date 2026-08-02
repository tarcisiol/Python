linhas = [[], [], []]
for n in range(3):
    num = int(input(f'Digite um valor para a {n+1}°posição: '))
    linhas[0].append(num)
for n in range(3):
    n2 = int(input(f'Digite um valor para a {n+1}°posição: '))
    linhas[1].append(n2)
for n in range(3):
    n3 = int(input(f'Digite um valor para a {n+1}°posição: '))
    linhas[2].append(n3)
for l in range(3):
    for c in range(3):
        print(f'[{linhas[l][c]:^5}]', end='')
    print()