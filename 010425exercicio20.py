pares = 0
impares = 0
for c in range(10):
    n = int(input(f'Digite o {c+1}° número: '))
    parimpar = n % 2
    if parimpar == 0:
        pares += 1
    else:
        impares += 1
print(f'São no total {pares} números pares e {impares} impares')