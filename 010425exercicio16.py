n = int(input('Digite um número para calcular o fatorial: '))
r = 1
for i in range(2, n + 1):
    r = r * i
print(f'O resultado desse fatorial é: {r}')