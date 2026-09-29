usuarios = []
alimentos = []

def adicionar_usuario():
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    usuario = {
        "email": email,
        "senha": senha
    }

    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")

def entrar_sistema():
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print("Login realizado com sucesso!")
            registrar_alimento()
            return

    print("Email ou senha incorretos.")

def registrar_alimento(email):
    nome = input("Digite o nome do alimento: ")
    quantidade = input("Digite a quantidade: ")
    validade = input("Digite a data de validade: ")

    alimento = {
        "email": email,
        "nome": nome,
        "quantidade": quantidade,
        "validade": validade
    }
    
    alimento.append(alimento)

print("Alimento registrado com sucesso!") 

def listar_alimentos(email):
    encontrou = False

    print("\n--- SEUS ALIMENTOS ---")

    for alimento in alimentos:
        if alimento["email"] == email:
            print(f"Nome: {alimento['nome']}")
            print(f"Quantidade: {alimento['quantidade']}")
            print(f"Validade: {alimento['validade']}")
            print("----------------------")
            encontrou = True

    if not encontrou:
        print("Nenhum alimento cadastrado.")

def menu():
    while True:
        print("\n===== SISTEMA =====")
        print("1 - Cadastrar usuário")
        print("2 - Entrar")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()

        elif opcao == "2":
            entrar_sistema()

        elif opcao == "3":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")

menu()








