numeros_inseridos = 0
soma = 0
maior = 0
menor = 0
continuar = 's'

while continuar == 's':
    numero = int(input('Digite um numero: '))
    numeros_inseridos += 1
    soma = soma + numero
    
    if numeros_inseridos == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
    continuar = input('Deseja continuar? (s/n): ').strip().lower()

if numeros_inseridos > 0:
    media = soma / numeros_inseridos
    print(f'A MÉDIA ENTRE TODOS FOI: {media:.2f}')
    print(f'O MAIOR NUMERO DIGITADO FOI: {maior}')
    print(f'O MENOR NUMERO DIGITADO FOI: {menor}')