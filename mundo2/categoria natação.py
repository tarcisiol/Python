idade = int(input('Qual a idade do atleta? '))
if idade <= 9:
    print('Ele compete na categoria MIRIM.')
elif idade <=14:
    print('Ele compete na categoria INFANTIL.')
elif idade <= 19:
    print('Ele compete na categoria JUNIOR.')
elif idade <=20:
    print ('Ele compete na categoria SÊNIOR.')
elif idade >20:
    print('Ele compete na categoria MASTER.')