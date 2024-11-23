#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que identifique a idade
# de um atleta e mostre sua categoria:
#   Até 9 anos: MIRIM
#   Até 14 anos: INFANTIL
#   Até 19 anos: JÚNIOR
#   Até 25 anos: SÊNIOR
#   Acima de 25 anos: MASTER

idade=int(input('Idade do atleta:'))
if idade<=9:
    print('MIRIM')
elif idade<=14:
    print('INFANTIL')
elif idade<=19:
    print('JUNIOR')
elif idade<=25:
    print('SÊNIOR')
else:
    print('MASTER')
