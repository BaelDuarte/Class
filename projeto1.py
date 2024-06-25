#Crie um programa que imprime o fatorial de um número
valor_inicial = int(input('insira o valor a ser calculado'))
if valor_inicial > 0:
    fatorial = 1
for item in range(1, valor_inicial +1):
    fatorial = fatorial * item
print(fatorial)

    