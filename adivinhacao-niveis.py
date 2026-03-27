import random

print("Bem-vindo ao jogo de adivinhação!")
print("\nEscolha o nível de dificuldade:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 50)")
print("3 - Difícil (1 a 100)")

# Validação da escolha do nível
while True:
    try:
        escolha = int(input("\nDigite sua escolha (1, 2 ou 3): "))
        if escolha in [1, 2, 3]:
            break
        else:
            print("Opção inválida! Por favor, digite 1, 2 ou 3.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

# Define o intervalo e o número de tentativas baseado na dificuldade
if escolha == 1:
    nivel = "Fácil"
    minimo, maximo = 1, 10
    max_tentativas = 5
elif escolha == 2:
    nivel = "Médio"
    minimo, maximo = 1, 50
    max_tentativas = 7
else:  # escolha == 3
    nivel = "Difícil"
    minimo, maximo = 1, 100
    max_tentativas = 10

# Gera o número secreto dentro do intervalo escolhido
numero_secreto = random.randint(minimo, maximo)

print(f"\n🎮 Você escolheu o nível {nivel}!")
print(f"Tente adivinhar o número entre {minimo} e {maximo}. Você tem {max_tentativas} tentativas.\n")

# Loop do jogo com número de tentativas variável
for tentativa in range(max_tentativas):
    try:
        palpite = int(input(f"Tentativa {tentativa + 1}/{max_tentativas}. Digite seu palpite: "))
        
        # Verifica se o palpite está no intervalo válido
        if palpite < minimo or palpite > maximo:
            print(f"⚠️  Digite um número entre {minimo} e {maximo}!")
            continue
        
        # Verifica o palpite do jogador
        if palpite == numero_secreto:
            print(f"\n🎉 Parabéns! Você acertou o número em {tentativa + 1} tentativa(s)!")
            break
        elif palpite < numero_secreto:
            print("📈 Quase lá! Tente um número maior.")
        else:
            print("📉 Quase lá! Tente um número menor.")
        
        # Checa se esta é a última tentativa
        if tentativa == max_tentativas - 1:
            print(f"\n❌ Suas tentativas acabaram. O número era {numero_secreto}.")
    
    except ValueError:
        print("❌ Entrada inválida! Por favor, digite um número inteiro.")

print("\n🏁 Fim do jogo!")
