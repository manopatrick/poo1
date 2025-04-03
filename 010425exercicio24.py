senhas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
escolha = 0
for c in senhas:
    print(f'senha {c} foi chamada!')
    while True:
        escolha = int(input('Digite 1 para encerrar atendimento: '))
        if escolha == 1:
            break
        else:
            continue
    while True:
        escolha = int(input('Digite 0 para chamar o próximo: '))
        if escolha == 0:
            break
        else:
            continue
print('Todas a senhas foram chamadas!')