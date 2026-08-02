pares = []
impares = []
numeros = []
while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    if num %2==0:
        pares.append(num)
    elif num %2!=0:
        impares.append(num)
    resposta = input('Deseja adicionar mais numeros? [S/N]: ').lower()
    if resposta == 'n':
        break
print(f'A lista completa é {numeros}')
print(f'Os numeros pares digitados foram: {pares}')
print(f'Os numeros impares digitados foram {impares}')
