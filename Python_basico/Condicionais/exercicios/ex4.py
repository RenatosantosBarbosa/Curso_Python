# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim:
# Nota 9 ou 10: "Excelente!"
# Nota 7 ou 8: "Muito bom"
# Nota 5 ou 6: "Regular"
# Menor que 5: "Ruim"

nota_filme = float(input("Digite a sua avaliação do filme (0 a 10): "))

if nota_filme >= 9 :
    print("Excelente!")
elif nota_filme >= 7:
    print("Muito bom")
elif nota_filme >= 5:
    print("Regular")
else:
    print("Ruim")