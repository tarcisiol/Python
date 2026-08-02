n5 = 0
lista = []
while True:
    lista.append(int(input('Digite um numero para adicionar na lista: ')))
    resposta = input('Deseja adicionar mais numeros? [S/N]: ').lower()
    if resposta == 'n':
        break
print(f'Foram digitados {len(lista)} números')
print(f'A lista em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
     n5 +=1
     print(f'O numero 5 esta na lista e foi digitado {n5} vezes')
else:
    print('O numero 5 nao esta na lista')
