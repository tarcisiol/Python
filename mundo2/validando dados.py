sexo = 'a'
homem = 'm'
mulher = 'f'
while sexo != 'm' or sexo != 'f':
    sexo = input('digite o sexo usando M/F: ').lower()
    if sexo == 'm' or sexo == 'f':
        print('dado armazenado')
    else:
        print('dado invalido , repita.')
    