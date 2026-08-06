# 1. Entrada de Dados
qtd_tarefas = int(input("Digite quantas tarefas deseja cadastrar: "))

lista_tarefas = []

for i in range(qtd_tarefas):
    nome = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome)

# 2. Processamento com enumerate() e range()
banco_dados_tarefas = []

for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    # Lógica de progressão de dias baseada no ID (ex: id * 2)
    prazo_dias = id_tarefa * 2
    status = "Pendente"
    
    # Armazenando como tupla na lista do banco de dados
    banco_dados_tarefas.append((id_tarefa, nome_tarefa, prazo_dias, status))

# 3. Saída de Dados e Desempacotamento
print("\n--- RESUMO DO SISTEMA ---")

for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

print(f"\nTotal de tarefas gerenciadas: {len(banco_dados_tarefas)}")
