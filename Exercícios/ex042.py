#Exercício Python 042: Digite 3 números e veja se é possível formar um triângulo com arestas com essas medidas.
# Acrescente o recurso de mostrar que tipo de triângulo será formado:
#    EQUILÁTERO: todos os lados iguais
#    ISÓSCELES: dois lados iguais, um diferente
#    ESCALENO: todos os lados diferentes

a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
if a+b>c and a+c>b and b+c>a:
    print('Os seguimentos acima PODEM FORMAR um triângulo do tipo ')
    if a == b == c:
       print('EQUILÁTERO')
    if a != b !=c !=a:
        print('ESCALENO')
else:
    print('ÍSÓSCELES')