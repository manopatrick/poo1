p = input('Digite uma palavra: ').upper()
v = 0
for c in p:
    if c in ('AEIOU'):
        v = v + 1
print(f'A Quantidade de Vogais é: {v}')