# Solicita o peso do usuário em kg
peso = float(input("Digite o peso em kg: "))

# Solicita a altura do usuário em metros
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Classifica o IMC e exibe a mensagem
if imc < 18.5:
    print("Abaixo do peso.")
elif imc < 25:
    print("Peso normal.")
elif imc < 30:
    print("Sobrepeso.")
else:
    print("Obesidade.")

