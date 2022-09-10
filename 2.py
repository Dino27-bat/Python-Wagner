""" 
Algoritimo que verifica a senha inserida pelo usuário e retorna se a senha inserida está correta ou incorreta
Autor: Pedro Henrique Dezem 
Data: 05/09/2022 19:33 
"""
#Definindo a senha
senha_certa = "Senha123@"


while True:
    #Pedindo a senha para usuário
    senha = (input('Senha: '))

    #Verificando se a senha inserida está correta
    if senha == senha_certa:
        print('Você está logado')
        break
    else:
        print('Senha incorreta')