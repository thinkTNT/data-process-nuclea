import requests

# URL do site
url = 'https://nuclea.com.br'

# Solicitar as credenciais (precisa ser do AD)
usuario = "USR00715"
senha = "7I7!$M;;t8j("

# Criar uma sessão
sessao = requests.Session()

# Enviar uma solicitação POST com as credenciais do usuário
login_data = {
    'usuario': usuario,
    'senha': senha
}
response = sessao.post(url, data=login_data)

# Verificar se o login foi bem-sucedido
if "Bem-vindo" in response.text:
    print("Login com sucesso no portal")
    # Aqui você pode continuar a usar a sessão para acessar outras páginas autenticadas, se necessário.
else:
    print("Login falhou. Verifique suas credenciais.")
