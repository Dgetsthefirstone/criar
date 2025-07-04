usuarios = ['marcos','ana','gabriel']
while True:
    pergunta = input("gostaria de remover um dos usuário?\n")
    if pergunta.title() == "Sim":
        print(f'escolha um deles\n\t {usuarios}')
        
        
        pergunta2 = input("digite qual\n")
        
        if pergunta2.lower() in usuarios:
            usuarios.remove(pergunta2)
            print('o usuário foi removido com sucesso')
            print(usuarios)
            break
        else:
            print(f"o usuário que você está chamando não existe. Tente novamente")
                    

    
    elif pergunta.title() == 'nao' or pergunta.title() == 'não':
        print("obrigado por entrar")
        break
print('A sessão acabou')
