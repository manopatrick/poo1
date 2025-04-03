ValorCompra = float(input('Digite o valor total da compra: '))
resposta = str(input('Escolha as opções de gorgeta \n A - 10%\n B - 15%\n C - 20%\n')).upper()
gorjeta = 0
if resposta == 'A':
    gorjeta = ValorCompra * 0.10
elif resposta == 'B':
    gorjeta = ValorCompra * 0.15
elif resposta == 'C':
    gorjeta = ValorCompra * 0.2
else:
    print('Erro!')
print(f'O valor da gorjeta será: {gorjeta}')