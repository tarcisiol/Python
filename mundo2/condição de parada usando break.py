numeros_digitados = 0
soma = 0
numero = 0
while numero >=0:
    numero = int(input('Digite um numero: '))
    numeros_digitados +=1
    if numero == 999:
        break
    soma = soma + numero
print(f'Foram digitados {numeros_digitados} numeros e a soma entre eles foi {soma}')