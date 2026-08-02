lixeira = []
numeros = []
adicionar = 0
while True:
    adicionar = int(input('Digite um numero para adicionar: '))
    if adicionar in numeros:
        lixeira.append(adicionar)
        print('Numero repetido, não vou adicionar a lista')
    else:
        numeros.append(adicionar)
    resposta = input('Deseja adicionar mais numeros? [S/N]: ').strip().lower()
    if resposta == 'n':
        break
numeros.sort()
print(f'Os valores digitados foram: {numeros}')