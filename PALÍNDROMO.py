frase = str(input('Digite alguma frase;: ')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
inverso = junta[::-1]
print(f'O inverso de {junta} é {inverso}')
if junta == inverso:
    print('É PALINDROMO!!!')
else:
    print('NÃO é PALINDROMO!!!')
