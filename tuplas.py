9
# Definição implícita de uma tupla
tupla_implicita = (1, 2, 3, 4)

# Definição explícita de uma tupla
lista = [5, 6, 7, 8]
tupla_explicita = tuple(lista)

print("Tupla implícita:", tupla_implicita, "| Tipo:", type(tupla_implicita))
print("Tupla explícita:", tupla_explicita, "| Tipo:", type(tupla_explicita))


10
# Cria uma tupla
empresas = ("Google", "Facebook", "Amazon") 
# Tentativa de alteração 
empresas[1] = "Samsung" 

12
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")

print(frutas)

13
frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")

print(frutas)

14
# Definição de uma tupla
frutas = ("maçã", "banana", "laranja", "uva")

# Encontra o índice do elemento "laranja" na tupla
indice_laranja = frutas.index("laranja")

print("O índice de 'laranja' é:", indice_laranja)
