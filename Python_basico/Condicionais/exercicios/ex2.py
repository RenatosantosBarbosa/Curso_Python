# Verificação de Diferença: Crie um código que peça para o usuário inserir dois nomes. Depois verifique se os dois nomes são diferentes. Se forem, exiba "Os nomes digitados são diferentes.".

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

if nome1 == nome2:
    print("Os nomes são iguais.")

if nome1 != nome2:
    print("Os nomes digitados são diferentes.")