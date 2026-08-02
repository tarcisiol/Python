import random
import time
palpites = []
quant = int(input('Quantos jogos voce quer que eu crie? '))
for c in range(quant):
    palpites = [random.randint(0,60) , random.randint(0,60) , random.randint(0,60) , random.randint(0,60) ,random.randint(0,60) , random.randint(0,60)]
    palpites.clear
    print(f'Jogo {c+1} {sorted(palpites)}')
    time.sleep(2)
print('BOA SORTE!')