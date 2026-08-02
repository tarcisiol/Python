sistema = [[], [], [], []]
while True:
    nome = input('Nome: ')
    sistema[0].append(nome)
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    sistema[1].append([n1, n2])
    calcular = (n1 + n2) / 2
    sistema[3].append(calcular)
    alunos = sistema[0]
    notas = sistema[1]
    media = sistema[3]
    resposta = input('Quer continuar? [S/N] ').lower()
    if resposta == 'n':
        break
print('-=' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for c in range(len(alunos)):
    print(f'{c+1:<4}{alunos[c]:<10}{media[c]:>8.1f}')
print('-' * 26)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc]} são {notas[opc]}')
        print('-' * 26)
print('<<< VOLTE SEMPRE >>>')