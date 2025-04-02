numero = int(input("Digite um número inteiro: "))
contador = 0
for div in range(1, numero):
    if div % 2 == 1:
        contador += 1
if contador == 2 :
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} é um número primo.")
