# Peça para o usuário digitar um meio de transporte. Mostre uma mensagem conforme a entrada:
# "carro" → "Veículo terrestre"
# "bicicleta" → "Transporte sustentável"
# "avião" ou "helicóptero" → "Transporte aéreo"
# Qualquer outro → "Transporte desconhecido"

print("----------Veiculos---------- \n Carro \n Bicicleta \n Avião ou Helicoptero")
# print("Carro")
# print("Bicicleta")
# print("Avião ou Helicoptero")

transporte = str(input("Digite um meio de transporte: "))

match transporte:
    case "Carro":
        print("Veiculo terrestre")
    case "Bicicleta":
        print("Transporte sustentavel")
    case "Avião" | "Helicoptero":
        print("Transporte aereo")
    case _:
        print("Transporte desconhecido!")
