import random
numeros = (random.randint(0,10) , random.randint(0,10) , random.randint(0,10) , random.randint(0,10) )
numeros_em_ordem = sorted(numeros)
print(f'os numeros sorteados foram {numeros}')
print('---------------------------------------')
print (f'o menor valor sorteado foi {numeros_em_ordem[0]}')
print (f'o maior valor sorteado foi {numeros_em_ordem[3]}')