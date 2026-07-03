npc = 12
meunumero = 11
tentativas = 0
import random 
while meunumero != npc:
    npc = random.randint (0,11)
    meunumero =  int (input ('Qual numero voce vai escolher? '))
    tentativas +=1
    if meunumero == npc:
        print(f'voce acertou e fora necessarias {tentativas} tentativas.')


