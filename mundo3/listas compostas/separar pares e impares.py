numeros = [[] , []]
for n in range(0,8):
    num = int(input('Digite um numero: '))
    if num %2==0:
        numeros[0].append(num)
    elif num %2!=0:
        numeros[1].append(num)
print(f'Os numeros pares digitados foram: {numeros[0]}')
print(f'Os numeros impares digitados foram {numeros[1]}')