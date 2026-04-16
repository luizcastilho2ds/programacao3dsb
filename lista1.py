# Programa para verificar se um número pertence a uma lista

# Ler a quantidade de números
n = int(input("Quantos números você deseja adicionar? "))

# Criar uma lista vazia
numeros = []

# Ler n números e adicioná-los à lista
print(f"Digite {n} números inteiros:")
for i in range(n):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

# Exibir a lista
print(f"\nLista de números: {numeros}")

# Ler o número x para verificar
x = int(input("\nDigite um número para verificar se pertence à lista: "))

# Verificar se x pertence à lista
if x in numeros:
    print(f"✓ O número {x} pertence à lista!")
else:
    print(f"✗ O número {x} NÃO pertence à lista!")
