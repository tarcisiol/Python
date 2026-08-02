numeros = []
for l in range(1,6):
    numeros.append(int(input(f'Digite o {l}° valor: ')))
for pos , valor in enumerate(numeros , start=1):
    print(f'Voce digitou os numeros: {numeros}')
print(f'O maior numero digitado foi {max(numeros)} na posição {numeros.index(max(numeros))}')
print(f'O menor numero digitado foi {min(numeros)} na posição {numeros.index(min(numeros))}')
