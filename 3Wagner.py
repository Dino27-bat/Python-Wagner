""" 
Algoritmo que recebe o tamanhos dos lados de um triangulo e retorna a classificação do triângulo
Autor: Pedro Henrique Dezem 
Data: 06/09/2022 20:03
""" 

#Pedindo o tamanho dos lados do triângulo
pri_lado = int(input('Insira o tamanho do primeiro lado do triângulo: ')) 
seg_lado = int(input('Insira o tamanho do segundo lado do triângulo: '))
ter_lado = int(input('Insira o tamanho do terceiro lado do triângulo: '))

#Verificando a classificação do triângulo
if pri_lado == seg_lado and seg_lado == ter_lado:
    print('Equilátero')

elif pri_lado != seg_lado and seg_lado != ter_lado and pri_lado != ter_lado:
    print('Escaleno')

elif pri_lado == seg_lado and pri_lado != ter_lado or pri_lado == ter_lado and pri_lado != seg_lado or seg_lado == pri_lado and seg_lado != ter_lado or seg_lado == ter_lado and seg_lado != pri_lado or ter_lado == seg_lado and ter_lado != pri_lado or ter_lado == pri_lado and ter_lado != seg_lado:
    print('Isósceles')