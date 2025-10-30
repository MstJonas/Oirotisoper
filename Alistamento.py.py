from datetime import datetime

ano_nascimento= int(input('Qual é o seu ano de nascimento? '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
quanto_falta = 18 - idade
if idade < 18:
    print(f'A sua idade é {idade} anos\nE falta {quanto_falta} anos para o seu Alistamento.')
elif idade == 18:
    print(f'Sua idade é {idade} anos. Este ano é o seu ALISTAMENTO!')
elif idade > 18:
    alistamento = ano_nascimento + 18
    tempo_passado = ano_atual -alistamento
    print(f'Seu alistamento foi {alistamento}, e se passaram {tempo_passado} anos.')
