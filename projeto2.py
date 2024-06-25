#Faça um programa que gere um número aleatório entre 1 a 10 e peça que o usuario tente descobrir qual seja, o programa deve informar se o valor chutado foi acima ou abaixo do valor esperado.
import random
valor_gerado = random.randint(1,10) 
acertou = False
while acertou == False:
    valor_chutado = int(input('tente adivinhar qual valor eu gerei entre 1 e 10: '))
    if valor_chutado > valor_gerado:
        print('voce chutou wum valor muito alto, tente um valor menor')
    elif valor_chutado < valor_gerado:
        print('voce chutou um numero muito baixo, tente um valor maior')
    elif valor_chutado == valor_gerado:
        acertou = True
        print('parabéns!, voce acertou')
