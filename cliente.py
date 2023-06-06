import socket

def cliente():
    HOST = 'localhost'
    PORT = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    # Solicitar ao usuário os dados de registro
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    nome_completo = input("Digite o nome completo: ")
    idade = input("Digite a idade: ")

    # Concatenar os dados em uma string separada por '|'
    dados = f"{username}|{senha}|{nome_completo}|{idade}"

    # Enviar os dados para o servidor
    s.sendall(str.encode(dados))
    data = s.recv(1024)

    print('Resposta do servidor:', data.decode())

# Exemplo de uso
cliente()
