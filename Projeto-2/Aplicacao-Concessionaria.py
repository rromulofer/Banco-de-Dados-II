import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import *
from tkinter import ttk

banco = sqlite3.connect("concessionaria2.db")
cursor = banco.cursor()

# Função para atualizar moto
def atualizar_moto(cursor, banco):
    try:
        moto_id_para_atualizar = int(id_atualizar_entry.get())
        campo = campo_atualizar_entry.get()
        novo_valor = novo_valor_atualizar_entry.get()
        cursor.execute(f"UPDATE Moto SET {campo} = ? WHERE IDMoto = ?", (novo_valor, moto_id_para_atualizar))
        banco.commit()
        messagebox.showinfo("Sucesso", "Moto atualizada com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar moto: {erro}")

# Função para remover moto
def remover_moto(cursor, banco):
    try:
        moto_id_para_deletar = int(id_remover_entry.get())
        cursor.execute("DELETE FROM Moto WHERE IDMoto = ?", (moto_id_para_deletar,))
        banco.commit()
        messagebox.showinfo("Sucesso", "Moto removida com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao remover moto: {erro}")

# Função para adicionar moto
def adicionar_moto(cursor, banco):
    try:
        modelo = modelo_adicionar_entry.get()
        ano = int(ano_adicionar_entry.get())
        preco = float(preco_adicionar_entry.get())
        cor = cor_adicionar_entry.get()
        id_compra = int(id_compra_adicionar_entry.get()) if id_compra_adicionar_entry.get() else None
        cursor.execute("INSERT INTO Moto (Modelo, Ano, Preco, Cor, IDCompra) VALUES (?, ?, ?, ?, ?)",
                       (modelo, ano, preco, cor, id_compra))
        banco.commit()
        messagebox.showinfo("Sucesso", "Moto adicionada com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao adicionar moto: {erro}")

# # Função para consultar motos
# def consultar_moto(cursor, banco):
#     try:
#         cursor.execute("SELECT * FROM Moto")
#         resultados = cursor.fetchall()
#         resultado_text.config(state=tk.NORMAL)
#         resultado_text.delete("1.0", tk.END)
#         for resultado in resultados:
#             resultado_text.insert(tk.END, f"ID: {resultado[0]}, Modelo: {resultado[1]}, Ano: {resultado[2]}, "
#                                           f"Preço: {resultado[3]}, Cor: {resultado[4]}, IDCompra: {resultado[5]}\n")
#         resultado_text.config(state=tk.DISABLED)
#     except sqlite3.Error as erro:
#         messagebox.showerror("Erro", f"Erro ao consultar moto: {erro}")

def atualizar_cliente(cursor, banco):
    try:
        cliente_id_para_atualizar = int(id_atualizar_cliente_entry.get())
        campo = campo_atualizar_cliente_entry.get()
        novo_valor = novo_valor_atualizar_cliente_entry.get()
        cursor.execute(f"UPDATE Clientes SET {campo} = ? WHERE IDCliente = ?", (novo_valor, cliente_id_para_atualizar))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados do cliente atualizados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar dados do cliente: {erro}")

# Função para remover dados de Cliente
def remover_cliente(cursor, banco):
    try:
        cliente_id_para_deletar = int(id_remover_cliente_entry.get())
        cursor.execute("DELETE FROM Clientes WHERE IDCliente = ?", (cliente_id_para_deletar,))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados do cliente removidos com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao remover dados do cliente: {erro}")

# Função para adicionar dados de Cliente
def adicionar_cliente(cursor, banco):
    try:
        nome = nome_adicionar_cliente_entry.get()
        idade = int(idade_adicionar_cliente_entry.get())
        telefone = telefone_adicionar_cliente_entry.get()
        email = email_adicionar_cliente_entry.get()
        endereco = endereco_adicionar_cliente_entry.get()
        cursor.execute("INSERT INTO Clientes (Nome, Idade, Telefone, Email, Endereco) VALUES (?, ?, ?, ?, ?)",
                       (nome, idade, telefone, email, endereco))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados do cliente adicionados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao adicionar dados do cliente: {erro}")

# Função para atualizar dados de Compra
def atualizar_compra(cursor, banco):
    try:
        compra_id_para_atualizar = int(id_atualizar_compra_entry.get())
        campo = campo_atualizar_compra_entry.get()
        novo_valor = novo_valor_atualizar_compra_entry.get()
        cursor.execute(f"UPDATE Compra SET {campo} = ? WHERE IDCompra = ?", (novo_valor, compra_id_para_atualizar))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados da compra atualizados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar dados da compra: {erro}")

# Função para remover dados de Compra
def remover_compra(cursor, banco):
    try:
        compra_id_para_deletar = int(id_remover_compra_entry.get())
        cursor.execute("DELETE FROM Compra WHERE IDCompra = ?", (compra_id_para_deletar,))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados da compra removidos com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao remover dados da compra: {erro}")

# Função para adicionar dados de Compra
def adicionar_compra(cursor, banco):
    try:
        data_compra = data_compra_adicionar_entry.get()
        valor = float(valor_adicionar_compra_entry.get())
        id_cliente = int(id_cliente_adicionar_compra_entry.get())
        cursor.execute("INSERT INTO Compra (DataCompra, Valor, IDCliente) VALUES (?, ?, ?)",
                       (data_compra, valor, id_cliente))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados da compra adicionados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao adicionar dados da compra: {erro}")


# Crie uma instância do Tkinter
root = tk.Tk()
root.title("Sistema de Controle de Motos")

# Crie um Notebook para abas
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Aba para Moto
frame_moto = ttk.Frame(notebook)
notebook.add(frame_moto, text="Moto")

# Adicione widgets à aba Moto
# Formulário para atualizar moto
atualizar_frame = tk.Frame(frame_moto)
atualizar_frame.pack()
atualizar_label = tk.Label(atualizar_frame, text="Atualizar Moto")
atualizar_label.grid(row=0, column=0, columnspan=2)
id_atualizar_label = tk.Label(atualizar_frame, text="ID da Moto:")
id_atualizar_label.grid(row=1, column=0)
id_atualizar_entry = tk.Entry(atualizar_frame)
id_atualizar_entry.grid(row=1, column=1)
campo_atualizar_label = tk.Label(atualizar_frame, text="Campo a Atualizar:")
campo_atualizar_label.grid(row=2, column=0)
campo_atualizar_entry = tk.Entry(atualizar_frame)
campo_atualizar_entry.grid(row=2, column=1)
novo_valor_atualizar_label = tk.Label(atualizar_frame, text="Novo Valor:")
novo_valor_atualizar_label.grid(row=3, column=0)
novo_valor_atualizar_entry = tk.Entry(atualizar_frame)
novo_valor_atualizar_entry.grid(row=3, column=1)
atualizar_button = tk.Button(atualizar_frame, text="Atualizar", command=lambda: atualizar_moto(cursor, banco))
atualizar_button.grid(row=4, column=0, columnspan=2)

# Formulário para remover moto
remover_frame = tk.Frame(frame_moto)
remover_frame.pack()
remover_label = tk.Label(remover_frame, text="Remover Moto")
remover_label.grid(row=0, column=0, columnspan=2)
id_remover_label = tk.Label(remover_frame, text="ID da Moto:")
id_remover_label.grid(row=1, column=0)
id_remover_entry = tk.Entry(remover_frame)
id_remover_entry.grid(row=1, column=1)
remover_button = tk.Button(remover_frame, text="Remover", command=lambda: remover_moto(cursor, banco))
remover_button.grid(row=2, column=0, columnspan=2)

# Formulário para adicionar moto
adicionar_frame = tk.Frame(frame_moto)
adicionar_frame.pack()
adicionar_label = tk.Label(adicionar_frame, text="Adicionar Moto")
adicionar_label.grid(row=0, column=0, columnspan=2)
modelo_adicionar_label = tk.Label(adicionar_frame, text="Modelo:")
modelo_adicionar_label.grid(row=1, column=0)
modelo_adicionar_entry = tk.Entry(adicionar_frame)
modelo_adicionar_entry.grid(row=1, column=1)
ano_adicionar_label = tk.Label(adicionar_frame, text="Ano:")
ano_adicionar_label.grid(row=2, column=0)
ano_adicionar_entry = tk.Entry(adicionar_frame)
ano_adicionar_entry.grid(row=2, column=1)
preco_adicionar_label = tk.Label(adicionar_frame, text="Preço:")
preco_adicionar_label.grid(row=3, column=0)
preco_adicionar_entry = tk.Entry(adicionar_frame)
preco_adicionar_entry.grid(row=3, column=1)
cor_adicionar_label = tk.Label(adicionar_frame, text="Cor:")
cor_adicionar_label.grid(row=4, column=0)
cor_adicionar_entry = tk.Entry(adicionar_frame)
cor_adicionar_entry.grid(row=4, column=1)
id_compra_adicionar_label = tk.Label(adicionar_frame, text="ID da Compra (opcional):")
id_compra_adicionar_label.grid(row=5, column=0)
id_compra_adicionar_entry = tk.Entry(adicionar_frame)
id_compra_adicionar_entry.grid(row=5, column=1)
adicionar_button = tk.Button(adicionar_frame, text="Adicionar", command=lambda: adicionar_moto(cursor, banco))
adicionar_button.grid(row=6, column=0, columnspan=2)



# Aba para Cliente (exemplo de outra aba)
frame_cliente = ttk.Frame(notebook)
notebook.add(frame_cliente, text="Cliente")

# Formulário para atualizar dados de Cliente
atualizar_cliente_frame = tk.Frame(frame_cliente)
atualizar_cliente_frame.pack()
atualizar_cliente_label = tk.Label(atualizar_cliente_frame, text="Atualizar Dados do Cliente")
atualizar_cliente_label.grid(row=0, column=0, columnspan=2)
id_atualizar_cliente_label = tk.Label(atualizar_cliente_frame, text="ID do Cliente:")
id_atualizar_cliente_label.grid(row=1, column=0)
id_atualizar_cliente_entry = tk.Entry(atualizar_cliente_frame)
id_atualizar_cliente_entry.grid(row=1, column=1)
campo_atualizar_cliente_label = tk.Label(atualizar_cliente_frame, text="Campo a Atualizar:")
campo_atualizar_cliente_label.grid(row=2, column=0)
campo_atualizar_cliente_entry = tk.Entry(atualizar_cliente_frame)
campo_atualizar_cliente_entry.grid(row=2, column=1)
novo_valor_atualizar_cliente_label = tk.Label(atualizar_cliente_frame, text="Novo Valor:")
novo_valor_atualizar_cliente_label.grid(row=3, column=0)
novo_valor_atualizar_cliente_entry = tk.Entry(atualizar_cliente_frame)
novo_valor_atualizar_cliente_entry.grid(row=3, column=1)
atualizar_cliente_button = tk.Button(atualizar_cliente_frame, text="Atualizar", command=lambda: atualizar_cliente(cursor, banco))
atualizar_cliente_button.grid(row=4, column=0, columnspan=2)

# Formulário para remover dados de Cliente
remover_cliente_frame = tk.Frame(frame_cliente)
remover_cliente_frame.pack()
remover_cliente_label = tk.Label(remover_cliente_frame, text="Remover Dados do Cliente")
remover_cliente_label.grid(row=0, column=0, columnspan=2)
id_remover_cliente_label = tk.Label(remover_cliente_frame, text="ID do Cliente:")
id_remover_cliente_label.grid(row=1, column=0)
id_remover_cliente_entry = tk.Entry(remover_cliente_frame)
id_remover_cliente_entry.grid(row=1, column=1)
remover_cliente_button = tk.Button(remover_cliente_frame, text="Remover", command=lambda: remover_cliente(cursor, banco))
remover_cliente_button.grid(row=2, column=0, columnspan=2)

# Formulário para adicionar dados de Cliente
adicionar_cliente_frame = tk.Frame(frame_cliente)
adicionar_cliente_frame.pack()
adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Adicionar Dados do Cliente")
adicionar_cliente_label.grid(row=0, column=0, columnspan=2)
nome_adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Nome:")
nome_adicionar_cliente_label.grid(row=1, column=0)
nome_adicionar_cliente_entry = tk.Entry(adicionar_cliente_frame)
nome_adicionar_cliente_entry.grid(row=1, column=1)
idade_adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Idade:")
idade_adicionar_cliente_label.grid(row=2, column=0)
idade_adicionar_cliente_entry = tk.Entry(adicionar_cliente_frame)
idade_adicionar_cliente_entry.grid(row=2, column=1)
telefone_adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Telefone:")
telefone_adicionar_cliente_label.grid(row=3, column=0)
telefone_adicionar_cliente_entry = tk.Entry(adicionar_cliente_frame)
telefone_adicionar_cliente_entry.grid(row=3, column=1)
email_adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Email:")
email_adicionar_cliente_label.grid(row=4, column=0)
email_adicionar_cliente_entry = tk.Entry(adicionar_cliente_frame)
email_adicionar_cliente_entry.grid(row=4, column=1)
endereco_adicionar_cliente_label = tk.Label(adicionar_cliente_frame, text="Endereço:")
endereco_adicionar_cliente_label.grid(row=5, column=0)
endereco_adicionar_cliente_entry = tk.Entry(adicionar_cliente_frame)
endereco_adicionar_cliente_entry.grid(row=5, column=1)
adicionar_cliente_button = tk.Button(adicionar_cliente_frame, text="Adicionar", command=lambda: adicionar_cliente(cursor, banco))
adicionar_cliente_button.grid(row=6, column=0, columnspan=2)



# Aba para Compras (exemplo de outra aba)
frame_compra = ttk.Frame(notebook)
notebook.add(frame_compra, text="Compras")

# Formulário para atualizar dados de Compra
atualizar_compra_frame = tk.Frame(frame_compra)
atualizar_compra_frame.pack()
atualizar_compra_label = tk.Label(atualizar_compra_frame, text="Atualizar Dados da Compra")
atualizar_compra_label.grid(row=0, column=0, columnspan=2)
id_atualizar_compra_label = tk.Label(atualizar_compra_frame, text="ID da Compra:")
id_atualizar_compra_label.grid(row=1, column=0)
id_atualizar_compra_entry = tk.Entry(atualizar_compra_frame)
id_atualizar_compra_entry.grid(row=1, column=1)
campo_atualizar_compra_label = tk.Label(atualizar_compra_frame, text="Campo a Atualizar:")
campo_atualizar_compra_label.grid(row=2, column=0)
campo_atualizar_compra_entry = tk.Entry(atualizar_compra_frame)
campo_atualizar_compra_entry.grid(row=2, column=1)
novo_valor_atualizar_compra_label = tk.Label(atualizar_compra_frame, text="Novo Valor:")
novo_valor_atualizar_compra_label.grid(row=3, column=0)
novo_valor_atualizar_compra_entry = tk.Entry(atualizar_compra_frame)
novo_valor_atualizar_compra_entry.grid(row=3, column=1)
atualizar_compra_button = tk.Button(atualizar_compra_frame, text="Atualizar", command=lambda: atualizar_compra(cursor, banco))
atualizar_compra_button.grid(row=4, column=0, columnspan=2)

# Formulário para remover dados de Compra
remover_compra_frame = tk.Frame(frame_compra)
remover_compra_frame.pack()
remover_compra_label = tk.Label(remover_compra_frame, text="Remover Dados da Compra")
remover_compra_label.grid(row=0, column=0, columnspan=2)
id_remover_compra_label = tk.Label(remover_compra_frame, text="ID da Compra:")
id_remover_compra_label.grid(row=1, column=0)
id_remover_compra_entry = tk.Entry(remover_compra_frame)
id_remover_compra_entry.grid(row=1, column=1)
remover_compra_button = tk.Button(remover_compra_frame, text="Remover", command=lambda: remover_compra(cursor, banco))
remover_compra_button.grid(row=2, column=0, columnspan=2)

# Formulário para adicionar dados de Compra
adicionar_compra_frame = tk.Frame(frame_compra)
adicionar_compra_frame.pack()
adicionar_compra_label = tk.Label(adicionar_compra_frame, text="Adicionar Dados da Compra")
adicionar_compra_label.grid(row=0, column=0, columnspan=2)
data_compra_adicionar_compra_label = tk.Label(adicionar_compra_frame, text="Data da Compra (AAAA-MM-DD):")
data_compra_adicionar_compra_label.grid(row=1, column=0)
data_compra_adicionar_entry = tk.Entry(adicionar_compra_frame)
data_compra_adicionar_entry.grid(row=1, column=1)
valor_adicionar_compra_label = tk.Label(adicionar_compra_frame, text="Valor:")
valor_adicionar_compra_label.grid(row=2, column=0)
valor_adicionar_compra_entry = tk.Entry(adicionar_compra_frame)
valor_adicionar_compra_entry.grid(row=2, column=1)
id_cliente_adicionar_compra_label = tk.Label(adicionar_compra_frame, text="ID do Cliente:")
id_cliente_adicionar_compra_label.grid(row=3, column=0)
id_cliente_adicionar_compra_entry = tk.Entry(adicionar_compra_frame)
id_cliente_adicionar_compra_entry.grid(row=3, column=1)
adicionar_compra_button = tk.Button(adicionar_compra_frame, text="Adicionar", command=lambda: adicionar_compra(cursor, banco))
adicionar_compra_button.grid(row=4, column=0, columnspan=2)

# Execute o loop principal da GUI
root.mainloop()

# Fechando a conexão com o banco de dados
banco.close()

