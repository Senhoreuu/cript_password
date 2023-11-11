import os
import bcrypt

senha = None

def criptografar(nova_senha):
    global senha
    senha = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())

def comparar(senha_para_comparar):
    if not senha:
        return 0

    return bcrypt.checkpw(senha_para_comparar.encode(), senha)

def main():
    global senha

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    menu = """
    1. Criptografar senha
    2. Comparar senha
    3. Sair
    """

    while True:
        print(menu)
        opt = input("Digite a opção desejada: ")

        if opt == '1':
            criptografar(input("Digite a senha: "))
            print("Senha criptografada com sucesso")

        elif opt == '2':
            if not senha:
                print("Você não salvou nenhuma senha ainda!")
                continue

            senha_para_comparar = input("Digite a senha: ")

            if comparar(senha_para_comparar):
                print("Senha correta")
            else:
                print("Senha incorreta")

        elif opt == '3':
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida")

main()
