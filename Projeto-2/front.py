import sqlite3
import tkinter as tk
from tkinter import messagebox

# Função para atualizar dados
def atualizar_dados():
    try:
        moto_id_para_atualizar = int(id_atualizar_entry.get())
        campo = campo_atualizar_entry.get()
        novo_valor = novo_valor_atualizar_entry.get()
        cursor.execute(f"UPDATE Moto SET {campo} = ? WHERE IDMoto = ?", (novo_valor, moto_id_para_atualizar))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao atualizar dados: {erro}")

# Função para remover dados
def remover_dados():
    try:
        moto_id_para_deletar = int(id_remover_entry.get())
        cursor.execute("DELETE FROM Moto WHERE IDMoto = ?", (moto_id_para_deletar,))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados removidos com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao remover dados: {erro}")

# Função para adicionar dados
def adicionar_dados():
    try:
        modelo = modelo_adicionar_entry.get()
        ano = int(ano_adicionar_entry.get())
        preco = float(preco_adicionar_entry.get())
        cor = cor_adicionar_entry.get()
        id_compra = int(id_compra_adicionar_entry.get()) if id_compra_adicionar_entry.get() else None
        cursor.execute("INSERT INTO Moto (Modelo, Ano, Preco, Cor, IDCompra) VALUES (?, ?, ?, ?, ?)",
                       (modelo, ano, preco, cor, id_compra))
        banco.commit()
        messagebox.showinfo("Sucesso", "Dados adicionados com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao adicionar dados: {erro}")

# Função para consultar dados
def consultar_dados():
    try:
        cursor.execute("SELECT * FROM Moto")
        resultados = cursor.fetchall()
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete("1.0", tk.END)
        for resultado in resultados:
            resultado_text.insert(tk.END, f"ID: {resultado[0]}, Modelo: {resultado[1]}, Ano: {resultado[2]}, "
                                          f"Preço: {resultado[3]}, Cor: {resultado[4]}, IDCompra: {resultado[5]}\n")
        resultado_text.config(state=tk.DISABLED)
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao consultar dados: {erro}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Concessionária")

# Conexão com o banco de dados
banco = sqlite3.connect('concessionaria2.db')
cursor = banco.cursor()

# Formulário para atualizar dados
atualizar_frame = tk.Frame(janela)
atualizar_frame.pack()
atualizar_label = tk.Label(atualizar_frame, text="Atualizar Dados")
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
atualizar_button = tk.Button(atualizar_frame, text="Atualizar", command=atualizar_dados)
atualizar_button.grid(row=4, column=0, columnspan=2)

# Formulário para remover dados
remover_frame = tk.Frame(janela)
remover_frame.pack()
remover_label = tk.Label(remover_frame, text="Remover Dados")
remover_label.grid(row=0, column=0, columnspan=2)
id_remover_label = tk.Label(remover_frame, text="ID da Moto:")
id_remover_label.grid(row=1, column=0)
id_remover_entry = tk.Entry(remover_frame)
id_remover_entry.grid(row=1, column=1)
remover_button = tk.Button(remover_frame, text="Remover", command=remover_dados)
remover_button.grid(row=2, column=0, columnspan=2)

# Formulário para adicionar dados
adicionar_frame = tk.Frame(janela)
adicionar_frame.pack()
adicionar_label = tk.Label(adicionar_frame, text="Adicionar Dados")
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
adicionar_button = tk.Button(adicionar_frame, text="Adicionar", command=adicionar_dados)
adicionar_button.grid(row=6, column=0, columnspan=2)

# Área de exibição de resultados
resultado_text = tk.Text(janela, height=10, width=40)
resultado_text.config(state=tk.DISABLED)
resultado_text.pack()

# Executa a interface gráfica
janela.mainloop()

# Fechando a conexão com o banco de dados
banco.close()
