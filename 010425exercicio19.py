compras = []
while True:
    escolha = str(input('Adicione um item na lista (use 0 para parar): '))
    if escolha == '0':
        break
    else:
        compras.append(escolha)
print(f'Os itens da lista de compras são: {compras}')