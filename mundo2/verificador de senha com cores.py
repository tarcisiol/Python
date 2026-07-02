usuarioc = 'tarcisioL'
senhac = 'tarcisio123@'
nome = str(input('Qual o seu nome? '))
usuario = str(input('Qual o seu usuario? '))
senha = str(input('Qual a sua senha? '))
if usuario == usuarioc and senha == senhac:
    print (f'\033[0;32mSeus dado estão corretos, Seja Bem vindo {nome}!\033[m')
else:
    print ('\033[0;31mSeus dados estão incorretos, tente novamente.\033[m')