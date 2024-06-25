'''programa que informa se houve uma multa e qual o nivel de sua gravidade
sendo 80 km a velocidade maxima permitida e +10,+20,+30 sendo consideradas 
multas leves graves e gravissimas'''

velocidade = int(input('Insira a sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('nao houve multa')
elif velocidade >= velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('tomou multa leve')
elif velocidade >= velocidade_maxima and velocidade <= velocidade_maxima + 29:
    print('tomou multa grave')
elif velocidade >= velocidade_maxima and velocidade >= velocidade_maxima + 30:
    print('tomou multa gravissima')