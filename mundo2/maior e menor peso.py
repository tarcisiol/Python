maior_peso = 0
menor_peso = 0
for p in range(1,6):
    peso_atual = float(input(f'Digite o peso da {p}° pessoa: '))
    if menor_peso == 0:
        menor_peso = peso_atual
    if peso_atual < menor_peso:
        menor_peso = peso_atual
    if peso_atual > maior_peso:
        maior_peso = peso_atual
print(f'O maior peso digitado foi {maior_peso}')
print(f'O menor peso digitado foi {menor_peso}')
