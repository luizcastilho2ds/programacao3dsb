import random  # Importa a biblioteca random para gerar números aleatórios

# Gera um número aleatório entre 1 e 10 e armazena em 'numero_secreto'
numero_secreto = random.randint(1, 10)

tentativas = 0  # Inicializa o contador de tentativas do jogador
max_tentativas = 5  # Define o número máximo de tentativas permitidas

print("Bem-vindo ao jogo de adivinhação!")  # Exibe uma mensagem de boas-vindas
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")  # Instrui o jogador sobre o objetivo do jogo

# Loop do jogo que continua enquanto o jogador não atingir o limite de tentativas
while tentativas < max_tentativas:
    # Captura a entrada do usuário e a converte para um número inteiro
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas a cada palpite
    tentativas += 1

    # Verifica o palpite do jogador
    if palpite == numero_secreto:
        # Caso o palpite seja correto, exibe uma mensagem de sucesso e finaliza o jogo
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break  # Sai do loop, pois o jogador acertou

    elif palpite < numero_secreto:
        # Caso o palpite seja menor que o número secreto, sugere um palpite maior
        print("Quase lá! Tente um número maior.")

    else:
        # Caso o palpite seja maior que o número secreto, sugere um palpite menor
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restam, se ainda houver tentativas
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Se o loop terminar sem o jogador ter acertado, exibe uma mensagem de falha
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")
