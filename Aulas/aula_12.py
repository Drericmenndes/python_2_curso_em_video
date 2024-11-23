nome = str(input('Qual é o seu nome? ')).strip().lower()
if nome == 'eric':
 print('Que nome impressionante!')
elif nome == 'caleb' or nome == 'reinaldo' or nome == 'gustavo' or nome == 'bebê':
 print('Esses cara é foda!')
elif nome in ('bruna', 'beatriz', 'thaynara'):
 print('Belo nome feminino!')
else:
 print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}')
