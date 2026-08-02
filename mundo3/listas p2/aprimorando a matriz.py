linhas = [[], [], []]
spar = scol = 0
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
        if linhas[l][c] % 2 == 0:
            spar += linhas[l][c]
    print()
for l in range(3):
    scol += linhas[l][2]
mai = max(linhas[1])
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {scol}.')
print(f'O maior valor da segunda linha é {mai}.')