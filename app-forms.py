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
# FUNÇÃO SALVAR
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
# FUNÇÃO LIMPAR
# -------------------------

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# -------------------------
# JANELA PRINCIPAL
# -------------------------

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x300")
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
# NOME
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
# E-MAIL
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
# TELEFONE
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

botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    width=12,
    command=salvar_cliente
)

botao_salvar.grid(row=0, column=0, padx=10)


botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=12,
    command=limpar_formulario
)

botao_limpar.grid(row=0, column=1, padx=10)


# -------------------------
# INICIAR PROGRAMA
# -------------------------

janela.mainloop()


# Fecha o banco quando o programa terminar
conexao.close()
