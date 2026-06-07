import random 
npc = random.randint (1,2)
meunumero =  int (input ('Qual numero voce vai escolher? '))

if npc == meunumero:
    print('Voce acertou')
else:
    print('Voce errou')
    print(f'O numero sorteado foi: {npc}')
