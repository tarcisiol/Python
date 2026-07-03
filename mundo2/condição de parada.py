numero = 0
soma_dos_numeros = 0
quantos_digitados = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero !=999:
    quantos_digitados +=1
    soma_dos_numeros = soma_dos_numeros + numero
    numero = int(input('Digite um numero [999 para parar]: '))
print(f'foram digitados {quantos_digitados} numeros e a soma entre eles foi {soma_dos_numeros}')
