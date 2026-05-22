def calcular_media(numeros):
    soma = sum(numeros)
    return soma / len(numeros)

def main():
    numeros = [10, 20, 30, 40, 50]
    media = calcular_media(numeros)
    print(f"A média é: {media:.2f}")

if __name__ == "__main__":
    main()
