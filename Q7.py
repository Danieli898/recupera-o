chomem = 0
cmulher = 0

for i in range(0, 4):
  nome = input("Nome:")
  sexo = str(input('Sexo: '))

  if sexo == 'masculino' :
    chomem = chomem + 1 
    print (nome) 
    print(' Você é homem ')

  elif sexo == 'feminino':
    cmulher = cmulher + 1
    print (nome) 
    print ('Você é mulher')

print('o numero de mulheres é: {}'.format(cmulher))
print('o numero de homens é: %d' % chomem)