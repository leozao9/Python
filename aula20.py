primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor == segundo_valor:
    print('Os valores são iguais.')
elif primeiro_valor > segundo_valor:
    print('O primeiro valor é maior que o segundo.')
elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior que o primeiro')
    
# OUTRO JEITO:
"""
if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
"""