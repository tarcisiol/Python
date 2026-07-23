numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    escolher = int(input('Digite o numero entre 0 e 10: '))
    if 0 <= escolher <= 10:
        break
    print('erro , digite outro numero')
print(f'voce escolheu o numero {escolher} e ele escrito por extenso é {numeros[escolher]}')