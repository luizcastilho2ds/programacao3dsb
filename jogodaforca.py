# Jogo da Forca Melhorado com Métodos de String e Desenho Progressivo

def desenhar_forca(erros):
    """Desenha a forca com as partes do corpo conforme os erros aumentam"""
    desenhos = [
        # 0 erros
        """
           ------
           |    |
           |
           |
           |
           |
        --------""",
        # 1 erro - Cabeça
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------""",
        # 2 erros - Corpo
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------""",
        # 3 erros - Braço esquerdo
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------""",
        # 4 erros - Braço direito
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------""",
        # 5 erros - Perna esquerda
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------""",
        # 6 erros - Perna direita (Game Over)
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------"""
    ]
    return desenhos[erros]


def inicializar_jogo():
    """Inicializa as variáveis do jogo"""
    palavra_secreta = "GIRAFA"
    letras_acertadas = ["_"] * len(palavra_secreta)
    letras_tentadas = []
    tentativas = 0
    return palavra_secreta, letras_acertadas, letras_tentadas, tentativas


def processar_palpite(palpite, palavra_secreta, letras_acertadas, letras_tentadas):
    """Processa o palpite do jogador e retorna se acertou"""
    palpite = palpite.upper()
    
    # Validação: apenas uma letra
    if len(palpite.strip()) != 1 or not palpite.isalpha():
        print("Entrada inválida! Digite apenas UMA letra.")
        return None
    
    # Validação: já foi tentada
    if palpite in letras_tentadas:
        print(f"Você já tentou a letra '{palpite}'!")
        return None
    
    letras_tentadas.append(palpite)
    
    # Verifica se a letra está na palavra (usando find ou count)
    if palpite in palavra_secreta:
        print(f"✓ Acertou! A letra '{palpite}' está na palavra!")
        
        # Substitui as posições corretas (usando find e replace)
        indice = 0
        for letra in palavra_secreta:
            if palpite == letra:
                letras_acertadas[indice] = letra
            indice += 1
        return True
    else:
        print(f"✗ Errou! A letra '{palpite}' não está na palavra.")
        return False


def exibir_status(palavra_secreta, letras_acertadas, letras_tentadas, tentativas):
    """Exibe o status atual do jogo"""
    print("\n" + "="*50)
    print(f"Palavra: {' '.join(letras_acertadas)}")
    print(f"Erros: {tentativas}/6")
    
    # Usando count() para contar letras acertadas
    acertos = sum(1 for letra in letras_acertadas if letra != "_")
    print(f"Progresso: {acertos}/{len(palavra_secreta)} letras acertadas")
    
    if letras_tentadas:
        print(f"Letras tentadas: {', '.join(sorted(letras_tentadas))}")
    print("="*50 + "\n")


def main():
    """Função principal do jogo"""
    print("\n" + "🎮 BEM-VINDO AO JOGO DA FORCA! 🎮".center(50))
    print("="*50)
    
    palavra_secreta, letras_acertadas, letras_tentadas, tentativas = inicializar_jogo()
    
    while tentativas < 6 and "_" in letras_acertadas:
        # Mostra o desenho da forca
        print(desenhar_forca(tentativas))
        
        # Mostra o status do jogo
        exibir_status(palavra_secreta, letras_acertadas, letras_tentadas, tentativas)
        
        # Recebe o palpite
        palpite = input("Digite uma letra: ").strip()
        resultado = processar_palpite(palpite, palavra_secreta, letras_acertadas, letras_tentadas)
        
        # Processa o resultado
        if resultado is False:  # Errou
            tentativas += 1
        elif resultado is None:  # Entrada inválida
            continue
        
        print()
    
    # Resultado final
    print(desenhar_forca(tentativas))
    print("\n" + "="*50)
    
    if "_" not in letras_acertadas:
        print("🎉 PARABÉNS! Você ganhou! 🎉")
        print(f"A palavra era: {palavra_secreta}")
    else:
        print("💀 QUE PENA! Você perdeu! 💀")
        print(f"A palavra era: {palavra_secreta}")
    
    print("="*50 + "\n")


if __name__ == "__main__":
    main()

