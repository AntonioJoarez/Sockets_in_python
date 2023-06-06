import socket
import hashlib

def verificar_credenciais(username, senha):
    # Verificar se os dados atendem à política de identificadores e senhas
    # Aqui você pode implementar suas próprias regras de validação
    if len(username) >= 3 and len(senha) >= 6:
        return True
    return False

def registrar_usuario(username, senha, nome_completo, idade):
    # Realizar cálculo de hash para a senha
    hashed_senha = hashlib.sha256(senha.encode()).hexdigest()

    # Armazenar os dados de registro no servidor (em memória neste exemplo)
    usuario = {
        'username': username,
        'senha': hashed_senha,
        'nome_completo': nome_completo,
        'idade': idade
    }
    usuarios.append(usuario)

def servidor():
    HOST = 'localhost'
    PORT = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Aguardando conexão de um cliente')
    conn, ender = s.accept()

    print('Conectado em', ender)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Fechando a conexão')
            conn.close()
            break

        # Decodificar os dados recebidos do cliente
        decoded_data = data.decode()

        # Separar os dados em username, senha, nome completo e idade
        username, senha, nome_completo, idade = decoded_data.split('|')

        # Verificar as credenciais fornecidas pelo cliente
        if verificar_credenciais(username, senha):
            registrar_usuario(username, senha, nome_completo, idade)
            resposta = f'Registro bem-sucedido. Bem-vindo, {nome_completo} ({idade} anos).'
        else:
            resposta = 'Erro ao registrar. Verifique os dados fornecidos.'

        # Enviar resposta para o cliente
        conn.sendall(str.encode(resposta))

        # Mostrar informações do usuário e fechar a conexão
        print(f'Usuário logado: {nome_completo} ({idade} anos)')
        print('Fechando a conexão')
        conn.close()
        break

# Lista para armazenar os usuários registrados (em memória neste exemplo)
usuarios = []

# Exemplo de uso
servidor()
