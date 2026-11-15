# Criando um dicionário chamado pessoa.
# Dicionários armazenam dados no formato chave: valor.
pessoa = {
    "nome": "Renato",  # Chave "nome" armazena o valor "Renato".
    "idade": 17,       # Chave "idade" armazena o número 17.
    "cidade": "São Paulo",  # Chave "cidade" armazena "São Paulo".

    # A chave "profissoes" armazena uma lista com três profissões.
    "profissoes": ["Programador", "Designer", "Pintor"]
}


# pessoa["idade"] = 18
# Altera o valor associado à chave "idade" para 18.

# print(pessoa["idade"])
# Acessa e exibe o valor armazenado na chave "idade".

# del pessoa["cidade"]
# Remove completamente a chave "cidade" e seu respectivo valor.

# print(pessoa["profissoes"][1])
# Acessa a lista dentro do dicionário e exibe o elemento de índice 1.
# Resultado: Designer (lembrando que os índices começam em 0).

# print(pessoa.keys())
# Retorna todas as chaves existentes no dicionário.
# Resultado: dict_keys(['nome', 'idade', 'cidade', 'profissoes'])

# print(pessoa.values())
# Retorna todos os valores armazenados no dicionário.

# valores = list(pessoa.values())
# Transforma os valores do dicionário em uma lista.
# Isso permite acessar os valores utilizando índices.

# print(valores[2])
# Exibe o terceiro elemento da lista valores.
# Resultado: São Paulo.

# print(pessoa.items())
# Retorna todos os pares de chave e valor do dicionário.
# Cada par é apresentado como uma tupla.

# print(pessoa.get("Telefone", "Não existe"))
# Tenta acessar a chave "Telefone".
# Como ela não existe, retorna "Não existe".
# O get() evita um erro quando a chave não é encontrada.

# pop() remove uma chave do dicionário e retorna seu valor.
# Aqui, remove a chave "profissoes" e guarda sua lista na variável.
item_removido = pessoa.pop("profissoes")

# Exibe o conteúdo que foi removido do dicionário.
print(f"Itens removidos: {item_removido}")

# print(pessoa)
# Exibe o dicionário atualizado, sem a chave "profissoes".


# Criando outro dicionário chamado produto.
produto = {
    "nome": "Notebook",  # Nome do produto.
    "preco": 3000,       # Preço do produto.
    "estoque": 15        # Quantidade disponível no estoque.
}

# Acessa as chaves "estoque" e "nome" para montar uma mensagem.
# As informações são inseridas na frase utilizando uma f-string.
print(
    f"Ainda restam {produto['estoque']} unidades "
    f"do produto {produto['nome']}"
)
