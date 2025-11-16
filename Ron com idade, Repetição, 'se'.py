from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for pessoa in range(1, 5):
    nascimento = int(input(f'Em que ano a {pessoa}º pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade +=1
print(f'Ao todo, tivemos {maior_idade} pessoas maiores de idade.')
print(f'Ao todo, tivemos {menor_idade} pessoas menores de idade.')
