# Seu programa deve verificar se o usuário tem direito a frete grátis. As regras são:
# O valor da compra deve ser maior ou igual a 100
# E o cliente precisa estar cadastrado no programa de fidelidade
# Se as duas condições forem verdadeiras, mostre: "Frete grátis aplicado!"
# Caso contrário: "Frete não disponível gratuitamente."

valor_minimo_compra = 100
fidelidade = False

valor_compra = float(input("Digite o valor da sua compra: "))

if valor_compra >= valor_minimo_compra and fidelidade:
    print("Frete grátis aplicado!")
else:
    print("Frete grátis não disponivel gratuitamente.")