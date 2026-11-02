# Crie um menu com 3 opções:
# 1. Pizza
# 2. Sushi
# 3. Salada
# # O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."

print("----------Menu----------\n 1. Pizza \n 2. Sushi \n 3. Salada")
# print("1. Pizza")
# print("2. Sushi")
# print("3. Salada")

pedido = int(input("Escolha o numero do seu pedido (1 a 3): "))

match pedido:
    case 1:
        print("Pizza escolhido.")
    case 2:
        print("Sushi escolhido.")
    case 3:
        print("Salada escolhido.")
    case _:
        print("Opção invalida!")