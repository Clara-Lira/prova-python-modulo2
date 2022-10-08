peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura)**2

if imc <18.5:
    print('Você está abaixo do peso!')
elif imc >30:
  print('Você está obeso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está com o peso normal para adultos!')
else:
    print('Você está com sobrepeso!')