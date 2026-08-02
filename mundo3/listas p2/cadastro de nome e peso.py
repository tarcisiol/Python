total = 0
pessoas = [[] , []]
while True:
    nome = input('Digite o nome: ')
    pessoas[0].append(nome)
    total +=1
    peso = int(input('Digite o peso: '))
    pessoas[1].append(peso)
    parar = input('Deseja continuar? ').lower()
    maior_peso = max(pessoas[1])
    menor_peso = min(pessoas[1])
    posma = pessoas[1].index(max(pessoas[1]))
    posme = pessoas[1].index(min(pessoas[1]))
    if parar == 'n':
        break
print(f'O mais pesado é {pessoas[0][posma]} e pesa {maior_peso}')
print(f'O mais leve é {pessoas[0][posme]} e pesa {menor_peso}')
print(f'Foram cadastradas {total} pessoas.')