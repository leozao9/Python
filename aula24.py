# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  L E O N A R D O
# -8-7-6-5-4-3-2-1
# nome = 'Leonardo'
# print (nome[4])
# print (nome[-4])
# print('ardo' in nome)
# print('um' in nome)
# print(10 * '-')
# print('ardo' not in nome)
# print('um' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')