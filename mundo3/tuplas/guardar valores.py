vpares = 0
v9 = 0
numeros = (int(input('Digite o primeiro valor: ')) , int(input('Digite o segundo valor: ')) , int(input('Digite o terceiro valor: ')) , int(input('Digite o quarto valor: ')))
print('----------------')
print(f'voce digitou os numeros: {numeros}')
for cont in numeros:
    if cont ==9:
        v9 +=1
    elif cont %2==0:
        vpares +=1
print(f'o valor 3 apareceu na na {numeros.index(3)+1}° posição')
print(f'o valor 9 apareceu {v9} vezes')
print(f'foram digitados {vpares} pares')
    


