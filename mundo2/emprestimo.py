valordacasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Em quantos anos voce deseja pagar?'))
prestacao = valordacasa / (anos * 12)
percentual = (prestacao / salario) * 100
if percentual >30:
    print(f'\033[0;31mSeu emprestimo foi recusado, pois compromete {percentual} e o maximo é 30%\033[0;31m')
else:
    print(f'\033[0;32mSeu emprestimo foi aprovado.\033[0;32m')
