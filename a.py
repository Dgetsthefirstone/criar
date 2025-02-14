usuarios = ['marcos','ana','gabriel']
while True:
    pergunta = input("gostaria de remover um dos usuário?\n")
    if pergunta.title() == "Sim":
        print(f'escola um deles\n\t {usuarios}')
        
        
        pergunta2 = input("digite qual\n")
        for value in usuarios:
               if pergunta2.lower() == value:
                    usuarios.remove(value)
                    print('o usuário foi removido com sucesso')
                    print(usuarios)
                    continue
               else:
                    print(f"o usuário {pergunta2} que você está chamando não existe, tente novamente")
                    

    
    elif pergunta.title() == 'Não':
        print("obrigado por entrar")
        break
print('A cessão acabou')
