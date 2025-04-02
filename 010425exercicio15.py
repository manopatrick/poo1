n = int(input('Digite a quantidade de números que deseja calcular a média: '))
med = 0
for c in range(n):
    v = int(input(f'Digite o {c+1}° número: '))
    med = med + v
med = med / n
print(f'A média dos números escritos é {med}')