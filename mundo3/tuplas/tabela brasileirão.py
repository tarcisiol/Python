times = 'Palmeiras' , 'Flamengo' , 'Bragantino' , 'Fluminense' , 'Athletico-PR' , 'Bahia' , 'Coritiba' , 'São Paulo' , 'Botafogo' , 'EC Vitória' , 'Atlético-MG' , 'Corinthians' , 'Cruzeiro' , 'Internacional' , 'Santos' , 'Grêmio' , 'Vasco' , 'Mirassol' , 'Remo' , 'Chapecoense'
primeiros_colocados = (times[0:6])
ultimos_colocados = (times[-4::])
times_em_ordem_alfabetica = sorted(times)
print('---TABELA DO BRASILEIRÃO SERIE A---')
print(f'os primeiros colocados são {primeiros_colocados}')
print(f'os últimos colocados são {ultimos_colocados}')
print(f'os times em ordem alfabetica:{times_em_ordem_alfabetica}')
print(f'o Chapecoense está na posição: {times.index('Chapecoense')+1}')