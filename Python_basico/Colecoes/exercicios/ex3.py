# 🧪 Exercício 3 – Trabalhando com contagem e localização
# Dada a lista abaixo:
# nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]
# Mostre:
# Quantas vezes o nome Carla aparece
# Qual o índice da primeira vez que ele aparece

nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]

contagem = nomes.count("Carla")
indice = nomes.index("Carla")

print(f"O nome Carla apareceu {contagem} vezes na lista, e o primeiro nome apareceu no index {indice}")