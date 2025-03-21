nome = 'Leonardo Prado Mestrinel'
altura = 1.78
peso = 75
imc = (peso / (altura * altura))
# imc = peso / altura ** 2 isso daria o mesmo resultado, mas sem os parenteses

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e o seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

# IMC = peso / (altura x altura)

# Leonardo Prado Mestrinel tem 1.78 de altura,
# pesa 75 quilos e seu IMC é
# 23.671253629592222