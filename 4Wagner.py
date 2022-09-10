""" 
Algoritimo que faz um menu para o usuario escolher qual operação matematica quer fazer e retorna o resultado
Autor: Pedro Henrique Dezem 
Data: 07/09/2022 20:52 
""" 

#Loop com o menu
while True:
    v = int(input("Digite '1' para fazer uma Adição\nDigite '2' para fazer uma Subtração\nDigite '3' para fazer uma Multiplicação\nDigite '4' para fazer uma Divisão\nDigite '5' para Sair\n")) 
#Verificação de qual opção foi escolhida e a sua operação matematica
    if v == 1:
        v1 = int(input("Digite o primeriro valor da operação: "))
        v2 = int(input("Digite o segundo valor da operação: "))
        v3 = v1 + v2
        print("A soma de", v1, "e", v2, "é", v3, "\nA Tabuada de", v1, "é:\n", v1*1, "\n",  v1*2, "\n", v1*3, "\n", v1*4, "\n", v1*5, "\n", v1*6, "\n", v1*7, "\n", v1*8, "\n", v1*9, "\n", v1*10, "\n", "\nA Tabuada de", v2, "é:\n", v2*1, "\n",  v2*2, "\n", v2*3, "\n", v2*4, "\n", v2*5, "\n", v2*6, "\n", v2*7, "\n", v2*8, "\n", v2*9, "\n", v2*10, "\n", "\nA Tabuada de", v3, "é:\n", v3*1, "\n",  v3*2, "\n", v3*3, "\n", v3*4, "\n", v3*5, "\n", v3*6, "\n", v3*7, "\n", v3*8, "\n", v3*9, "\n", v3*10, "\n")
    if v == 2:
        v1 = int(input("Digite o primeriro valor da operação: "))
        v2 = int(input("Digite o segundo valor da operação: "))
        v3 = v1 - v2
        print("A subtração de", v1, "e", v2, "é", v3, "\nA Tabuada de", v1, "é:\n", v1*1, "\n",  v1*2, "\n", v1*3, "\n", v1*4, "\n", v1*5, "\n", v1*6, "\n", v1*7, "\n", v1*8, "\n", v1*9, "\n", v1*10, "\n", "\nA Tabuada de", v2, "é:\n", v2*1, "\n",  v2*2, "\n", v2*3, "\n", v2*4, "\n", v2*5, "\n", v2*6, "\n", v2*7, "\n", v2*8, "\n", v2*9, "\n", v2*10, "\n", "\nA Tabuada de", v3, "é:\n", v3*1, "\n",  v3*2, "\n", v3*3, "\n", v3*4, "\n", v3*5, "\n", v3*6, "\n", v3*7, "\n", v3*8, "\n", v3*9, "\n", v3*10, "\n")
    if v == 3:
        v1 = int(input("Digite o primeriro valor da operação: "))
        v2 = int(input("Digite o segundo valor da operação: "))
        v3 = v1 * v2
        print("A multiplicação de", v1, "e", v2, "é", v3, "\nA Tabuada de", v1, "é:\n", v1*1, "\n",  v1*2, "\n", v1*3, "\n", v1*4, "\n", v1*5, "\n", v1*6, "\n", v1*7, "\n", v1*8, "\n", v1*9, "\n", v1*10, "\n", "\nA Tabuada de", v2, "é:\n", v2*1, "\n",  v2*2, "\n", v2*3, "\n", v2*4, "\n", v2*5, "\n", v2*6, "\n", v2*7, "\n", v2*8, "\n", v2*9, "\n", v2*10, "\n", "\nA Tabuada de", v3, "é:\n", v3*1, "\n",  v3*2, "\n", v3*3, "\n", v3*4, "\n", v3*5, "\n", v3*6, "\n", v3*7, "\n", v3*8, "\n", v3*9, "\n", v3*10, "\n")
    if v == 4:
        v1 = int(input("Digite o primeriro valor da operação: "))
        v2 = int(input("Digite o segundo valor da operação: "))
        v3 = v1 / v2
        print("A divisão de", v1, "e", v2, "é", v3, "\nA Tabuada de", v1, "é:\n", v1*1, "\n",  v1*2, "\n", v1*3, "\n", v1*4, "\n", v1*5, "\n", v1*6, "\n", v1*7, "\n", v1*8, "\n", v1*9, "\n", v1*10, "\n", "\nA Tabuada de", v2, "é:\n", v2*1, "\n",  v2*2, "\n", v2*3, "\n", v2*4, "\n", v2*5, "\n", v2*6, "\n", v2*7, "\n", v2*8, "\n", v2*9, "\n", v2*10, "\n", "\nA Tabuada de", v3, "é:\n", v3*1, "\n",  v3*2, "\n", v3*3, "\n", v3*4, "\n", v3*5, "\n", v3*6, "\n", v3*7, "\n", v3*8, "\n", v3*9, "\n", v3*10, "\n")
    if v == 5:
        print("Tchau!")
        break
    if v == 0 or v > 5:
        print("\nDigite um número de '1' a '5'\n")