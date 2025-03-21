# Lista da ordem dos mais fortes aos mais fracos que serão resolvidos nas contas
# 1. (n + n) Sempre resolvido de dentro para fora
# 2. **
# 3. * / // %
# 4. + -

# conta_1 = 1 + 1 ** 5 + 5 Caso seja feito assim o resuldado estará errado
# sera feito desta forma 1 + 1 + 5 = 7
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) 
print(conta_1)