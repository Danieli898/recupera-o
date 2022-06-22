nome = str (input("nome do aluno:"))
n1 = float (input("nota um:"))
n2 = float (input("nota dois:"))
n3 = float (input("nota tres:"))
media = (n1+n2+n3) /3

print (" média do aluno: {}" .format(media))

if media >= 7:
    print ("APROVADO!")
    
elif media <= 5:
    print ("REPROVADO!")
    
else :
    print ("RECUPERAÇÃO")