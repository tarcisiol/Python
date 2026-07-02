nasceu = int(input('Em qual ano voce nasceu? '))
anoatual = 2026
idadeatual = anoatual - nasceu
anodoalistamento = nasceu + 18
deveria = anodoalistamento - anoatual
print (f'Quem nasceu em {nasceu} tem {idadeatual} anos em {anoatual}')
if anodoalistamento < anoatual:
    print (f'Seu alistamento deveria ter sido no ano de {anodoalistamento}')
else:
    print (f'Seu ano de alistamento é no ano de {anodoalistamento}')
