maior = 0
menor = 0
for k in range(1,5):
    peso = float(input(f'Digite o peso da {k}º pessoa:'))
    if k == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}\nEnquanto que o menor foi {menor}')
