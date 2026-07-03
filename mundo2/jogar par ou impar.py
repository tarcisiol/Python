import random 
meu_numero = 0
numero_do_pc = 0
vitorias = 0
derrotas = 0
escolha = 'par' or 'impar'
while True:
    meu_numero = int(input('Digite um valor: '))
    escolha = input ('Escolha Par ou Impar: ').lower()
    numero_do_pc = random.randint (0,11)
    if escolha == 'par':
        if (meu_numero + numero_do_pc) %2==0:
            vitorias +=1
            print(f'voce ganhou')
            print(f'o computador escolheu o numero {numero_do_pc}')
            print(f'a soma de {meu_numero} + {numero_do_pc} é {meu_numero + numero_do_pc}')
            print(f'voce ganhou {vitorias} vezes')
        else:
            print(f'voce perdeu')
            print(f'o computador escolheu o numero {numero_do_pc}')
            print(f'a soma de {meu_numero} + {numero_do_pc} é {meu_numero + numero_do_pc}')
            break
    elif escolha == 'impar':
        if (meu_numero + numero_do_pc) %2!=0:
            vitorias +=1
            print(f'voce ganhou')
            print(f'o computador escolheu o numero {numero_do_pc}')
            print(f'a soma de {meu_numero} + {numero_do_pc} é {meu_numero + numero_do_pc}')
            print(f'voce ganhou {vitorias} vezes')
        else:
            print(f'voce perdeu')
            print(f'o computador escolheu o numero {numero_do_pc}')
            print(f'a soma de {meu_numero} + {numero_do_pc} é {meu_numero + numero_do_pc}')
            break