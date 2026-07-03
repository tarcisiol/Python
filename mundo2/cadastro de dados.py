sexo = 'm' or 'f'
idade = 0
maisde18 = 0
mulheres20 = 0
homens = 0
continuar = 's'
while continuar == 's':
    print('INFORME OS DADOS A SEGUIR:')
    sexo = input('Qual o sexo da pessoa? (M/F): ').lower()
    idade = int(input('Qual a idade da pessoa? '))
    if sexo == 'm':
        homens +=1
    if sexo == 'f' and idade < 20:
            mulheres20 +=1
    if sexo == 'm' or 'f' and idade >=18:
            maisde18 +=1
    continuar = input('Deseja cadastrar outra pessoa? (S/N): ').lower()
    if continuar == 'n':
        break
print(f'TEM {maisde18} PESSOAS TEM MAIS DE 18')
print(f'FORAM CADASTRADOS {homens} HOMENS')
print(f'{mulheres20} MULHERES TEM MENOS DE 20 ANOS')
    

