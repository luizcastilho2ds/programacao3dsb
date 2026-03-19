"""
Calculadora de Desconto
Programa que solicita o preço de um produto e um código de desconto (A, B ou C)
e aplica o desconto correspondente, exibindo o preço final.
"""

def aplicar_desconto(preco, codigo):
    """
    Aplica desconto ao preço baseado no código fornecido.
    
    Código A: 10% de desconto
    Código B: 20% de desconto
    Código C: 30% de desconto
    
    Args:
        preco (float): Preço do produto
        codigo (str): Código de desconto (A, B ou C)
    
    Returns:
        tuple: (preco_desconto, preco_final)
    """
    desconto_percentual = 0
    
    if codigo.upper() == 'A':
        desconto_percentual = 10
    elif codigo.upper() == 'B':
        desconto_percentual = 20
    elif codigo.upper() == 'C':
        desconto_percentual = 30
    else:
        print("Código de desconto inválido! Códigos aceitos: A, B ou C")
        return None, preco
    
    preco_desconto = (preco * desconto_percentual) / 100
    preco_final = preco - preco_desconto
    
    return preco_desconto, preco_final


def main():
    """Função principal do programa."""
    print("=" * 50)
    print("        CALCULADORA DE DESCONTO")
    print("=" * 50)
    print("\nCódigos de desconto disponíveis:")
    print("  A - 10% de desconto")
    print("  B - 20% de desconto")
    print("  C - 30% de desconto")
    print("-" * 50)
    
    try:
        # Solicita o preço
        preco = float(input("\nDigite o preço do produto (R$): "))
        
        if preco < 0:
            print("Erro: O preço não pode ser negativo!")
            return
        
        # Solicita o código de desconto
        codigo = input("Digite o código de desconto (A/B/C): ")
        
        # Aplica o desconto
        desconto, preco_final = aplicar_desconto(preco, codigo)
        
        if desconto is not None:
            # Exibe os resultados
            print("\n" + "=" * 50)
            print("RESULTADO:")
            print("=" * 50)
            print(f"Preço original:    R$ {preco:.2f}")
            print(f"Código desconto:   {codigo.upper()}")
            print(f"Valor do desconto: R$ {desconto:.2f}")
            print(f"Preço final:       R$ {preco_final:.2f}")
            print("=" * 50)
        
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o preço!")


if __name__ == "__main__":
