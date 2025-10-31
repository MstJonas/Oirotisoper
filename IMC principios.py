peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura ** 2)
print(f'O seu IMC É {imc:.2f} e você está com o indice:',end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 24.9:
    print('PESO NORMAL')
elif 25 <= imc <= 29.9:
    print('SOBRE-PESO')
elif 30 <= imc <= 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
