# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.
# Se o usuário e a senha estão corretos → "Login bem-sucedido"
# Senão → "Usuário ou senha incorretos"

dicionario_correto = {
    'usuario': 'RNT',
    'senha': 735
}
dicionario_entrada = {
    'usuario': input("Digite seu usuário: "),
    'senha': int(input("Digite sua senha: "))
}

if dicionario_entrada['usuario'] == dicionario_correto['usuario'] and dicionario_entrada['senha'] == dicionario_correto['senha']:
    print("Acesso liberado! Pode entrar!")
else:
    print("Credenciais incorretas. Tente novamente.")