import tkinter as tk
from tkinter import messagebox
import sqlite3

# -------------------------
# BANCO DE DADOS
# -------------------------

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# -------------------------
# FUNÇÃO SALVAR CLIENTE
# -------------------------

def salvar_cliente():
    nome = entrada_nome.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()

    # Verifica se todos os campos foram preenchidos
    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    # Salva os dados no banco
    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
    """, (nome, email, telefone))

    conexao.commit()

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

    limpar_formulario()


# -------------------------
# FUNÇÃO LIMPAR FORMULÁRIO
# -------------------------

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# -------------------------
# FUNÇÃO VISUALIZAR CLIENTES
# -------------------------

def visualizar_clientes():

    # Cria uma nova janela
    janela_clientes = tk.Toplevel(janela)

    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("600x400")

    # Título
    tk.Label(
        janela_clientes,
        text="Clientes Cadastrados",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    # Área onde os clientes serão exibidos
    lista_clientes = tk.Text(
        janela_clientes,
        width=70,
        height=15
    )

    lista_clientes.pack(padx=10, pady=10)

    # Busca todos os clientes no banco
    cursor.execute("""
        SELECT id, nome, email, telefone
        FROM clientes
    """)

    clientes = cursor.fetchall()

    # Verifica se existem clientes
    if len(clientes) == 0:
        lista_clientes.insert(
            tk.END,
            "Nenhum cliente cadastrado."
        )
    else:
        # Exibe os clientes
        for cliente in clientes:

            id_cliente = cliente[0]
            nome = cliente[1]
            email = cliente[2]
            telefone = cliente[3]

            lista_clientes.insert(
                tk.END,
                f"ID: {id_cliente}\n"
                f"Nome: {nome}\n"
                f"E-mail: {email}\n"
                f"Telefone: {telefone}\n"
                f"{'-' * 50}\n"
            )

    # Impede que o usuário altere os dados exibidos
    lista_clientes.config(state=tk.DISABLED)


# -------------------------
# JANELA PRINCIPAL
# -------------------------

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("400x350")
janela.resizable(False, False)


# -------------------------
# TÍTULO
# -------------------------

titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=20)


# -------------------------
# CAMPO NOME
# -------------------------

tk.Label(
    janela,
    text="Nome:"
).pack()

entrada_nome = tk.Entry(
    janela,
    width=40
)

entrada_nome.pack(pady=5)


# -------------------------
# CAMPO E-MAIL
# -------------------------

tk.Label(
    janela,
    text="E-mail:"
).pack()

entrada_email = tk.Entry(
    janela,
    width=40
)

entrada_email.pack(pady=5)


# -------------------------
# CAMPO TELEFONE
# -------------------------

tk.Label(
    janela,
    text="Telefone:"
).pack()

entrada_telefone = tk.Entry(
    janela,
    width=40
)

entrada_telefone.pack(pady=5)


# -------------------------
# BOTÕES
# -------------------------

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)


# Botão Salvar
botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    width=12,
    command=salvar_cliente
)

botao_salvar.grid(row=0, column=0, padx=5)


# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=12,
    command=limpar_formulario
)

botao_limpar.grid(row=0, column=1, padx=5)


# Botão Visualizar Clientes
botao_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    width=25,
    command=visualizar_clientes
)

botao_visualizar.pack(pady=5)


# -------------------------
# INICIAR PROGRAMA
# -------------------------

janela.mainloop()


# Fecha o banco de dados
conexao.close()
