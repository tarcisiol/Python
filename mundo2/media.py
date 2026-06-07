n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1 + n2) / 2
if media < 5:
    print ('\033[0;31mREPROVADO\033[0;31m')
elif media >= 7:
    print ('\033[0;34mAPROVADO\033[0;34m')
elif 5.0 <= media <= 6.9:
    print ('\033[0;33mRECUPERAÇÃO\033[0;33m')