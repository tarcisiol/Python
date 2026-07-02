frase = input('Digite uma frase: ')
inverso = frase[::-1]
inverso_sem_espacos = ''.join(inverso.split())
frase_sem_espacos = ''.join(frase.split())
if frase_sem_espacos.lower() == inverso_sem_espacos.lower():
    print('isso é um palindromo')
else:
    print(f'isso não é um palindromo, o inverso seria {inverso_sem_espacos}')