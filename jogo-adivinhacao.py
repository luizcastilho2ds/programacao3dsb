import random

def jogo_adivinhacao():
    """
    Jogo de adivinhação com sistema de bônus de tentativas.
    O jogador tem 5 tentativas para descobrir um número entre 1 e 10.
    Ganha +1 tentativa ao acertar diferença de apenas 1 unidade.
    """
    numero_secreto = random.randint(1, 10)
    tentativas_maximas = 5
    tentativa_atual = 0
    
    print("=" * 50)
    print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("=" * 50)
    print(f"Adivinhe um número entre 1 e 10")
    print(f"Você tem {tentativas_maximas} tentativas para acertar!")
    print("=" * 50)
    
    while tentativa_atual < tentativas_maximas:
        tentativa_atual += 1
        
        try:
            numero_usuario = int(input(f"\nTentativa {tentativa_atual}/{tentativas_maximas}: Digite um número: "))
            
            # Validação do intervalo
            if numero_usuario < 1 or numero_usuario > 10:
                print("❌ Por favor, digite um número entre 1 e 10!")
                tentativa_atual -= 1  # Não conta como tentativa válida
                continue
            
            # Verifica se acertou
            if numero_usuario == numero_secreto:
                print(f"\n🎉 PARABÉNS! Você acertou! O número era {numero_secreto}!")
                print(f"Você venceu em {tentativa_atual} tentativa(s)!")
                return True
            
            # Verifica se está muito perto (diferença de 1)
            diferenca = abs(numero_usuario - numero_secreto)
            
            if diferenca == 1:
                print(f"🔥 MUITO QUENTE! Você está a apenas 1 número de distância!")
                print(f"💡 Você ganhou +1 tentativa de bônus!")
                tentativas_maximas += 1
            elif diferenca <= 3:
                print(f"🌡️ Quente! Você está perto (diferença: {diferenca})")
            else:
                print(f"❄️ Frio! Você está longe (diferença: {diferenca})")
            
            # Dica adicional
            if numero_usuario < numero_secreto:
                print("📈 Dica: O número secreto é MAIOR que o seu palpite")
            else:
                print("📉 Dica: O número secreto é MENOR que o seu palpite")
        
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número válido.")
            tentativa_atual -= 1  # Não conta como tentativa válida
            continue
    
    # Fim do jogo - jogador perdeu
    print(f"\n😢 Fim do jogo! Você não conseguiu adivinhar.")
    print(f"O número secreto era: {numero_secreto}")
    return False

# Executar o jogo
if __name__ == "__main__":
    resultado = jogo_adivinhacao()
    print("\n" + "=" * 50)
    if resultado:
        print("STATUS: VITÓRIA! ✨")
    else:
        print("STATUS: DERROTA! 💔")
    print("=" * 50)
