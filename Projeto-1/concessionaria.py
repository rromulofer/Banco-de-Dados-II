import sqlite3

# Conectando ao banco de dados (será criado se não existir)
banco = sqlite3.connect('concessionaria2.db')

# "Ponte" entre o python e o banco de dados, usado para executar comandos
cursor = banco.cursor()


# # Criando a tabela de CLIENTE
# cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
#                 IDCliente INTEGER PRIMARY KEY,
#                 Nome TEXT NOT NULL,
#                 Idade INTEGER,
#                 Telefone TEXT,
#                 Email TEXT,
#                 Endereco TEXT
#             );''')

# # Criando a tabela de COMPRA
# cursor.execute('''CREATE TABLE IF NOT EXISTS Compra (
#                 IDCompra INTEGER PRIMARY KEY,
#                 DataCompra TEXT,
#                 Valor REAL,
#                 IDCliente INTEGER,
#                 FOREIGN KEY (IDCliente) REFERENCES Clientes (IDCliente)
#             );''')

# # Criando a tabela de MOTO
# cursor.execute('''CREATE TABLE IF NOT EXISTS Moto (
#                 IDMoto INTEGER PRIMARY KEY,
#                 Modelo TEXT,
#                 Ano INTEGER,
#                 Preco REAL,
#                 Cor TEXT,
#                 IDCompra INTEGER,
#                 FOREIGN KEY (IDCompra) REFERENCES Compra (IDCompra)
#             );''')


# # Inserindo dados na tabela de Clientes
# clientes_data = [
#     ('João Silva', 30,'111-1111', 'joao@gmail.com', 'Rua A, 123'),
#     ('Maria Souza', 45,'222-2222', 'maria@gmail.com', 'Avenida B, 456'),
#     ('Carlos Oliveira', 17,'333-3333', 'carlos@gmail.com', 'Rua X, 789'),
#     ('Ana Rodrigues', 61,'777-8888', 'ana@gmail.com', 'Avenida Y, 101'),
#     ('Paulo Santos', 25,'999-0000', 'paulo@gmail.com', 'Praça Z, 222'),
#     ('Fernanda Lima', 34,'222-3333', 'fernanda@gmail.com', 'Estrada W, 333'),
#     ('Laura Mendes', 28, '444-4444', 'laura@gmail.com', 'Alameda C, 567'),
#     ('Giovane Pereira', 39, '555-5555', 'giovane@gmail.com', 'Travessa D, 890'),
#     ('Mariana Oliveira', 29, '666-6666', 'mariana@gmail.com', 'Avenida E, 1234'),
#     ('Pedro Fernandes', 42, '777-7777', 'pedro@gmail.com', 'Rua F, 5678'),
# ]
# cursor.executemany("INSERT INTO Clientes (Nome, Idade, Telefone, Email, Endereco) VALUES (?, ?, ?, ?, ?)", clientes_data)


# # Inserindo dados na tabela de Compra
# compra_data = [
#     ('2023-08-20', 32000.0, 1),  
#     ('2023-08-21', 45000.0, 2),  
#     ('2023-08-22', 44000.0, 3),
#     ('2023-08-23', 38000.0, 4),  
#     ('2023-08-24', 50000.0, 5),  
#     ('2023-08-25', 48000.0, 6),
#     ('2023-08-26', 90000.0, 7),
#     ('2023-08-27', 75000.0, 8), 
#     ('2023-08-28', 67000.0, 9), 
#     ('2023-08-29', 60000.0, 10),
# ]
# cursor.executemany("INSERT INTO Compra (DataCompra, Valor, IDCliente) VALUES (?, ?, ?)", compra_data)


# # Inserindo dados na tabela de Moto
# moto_data = [
#     ('Ninja 300', 2022, 32000.0, 'Azul', 1),  
#     ('CBR 650R', 2021, 45000.0, 'Vermelho', 2),  
#     ('MT-07', 2023, 44000.0, 'Preto', 3),  
#     ('YZF-R6', 2022, 38000.0, 'Branco', 4),  
#     ('Duke 390', 2023, 50000.0, 'Laranja', 5),  
#     ('GSX-S750', 2021, 48000.0, 'Preto', 6),
#     ('Ducati Panigale', 2022, 90000.0, 'Branco', 7),
#     ('CBR600RR', 2021, 75000.0, 'Vermelho', 8),
#     ('Kawasaki Z900', 2021, 67000.0, 'Preto', 9),
#     ('Ninja 400', 2022, 60000.0, 'Verde', 10),
#     ('CBR 1000RR', 2023, 85000.0, 'Vermelho', None),
#     ('GSX-R1000', 2023, 89000.0, 'Azul', None),
#     ('Ninja ZX-10R', 2023, 92000.0, 'Verde', None),
#     ('Ducati Panigale V4', 2023, 98000.0, 'Branco', None),
#     ('MT-09', 2023, 55000.0, 'Preto', None),
#     ('CB650R', 2023, 58000.0, 'Amarelo', None),
#     ('YZF-R1', 2023, 96000.0, 'Laranja', None),
#     ('Monster 821', 2023, 75000.0, 'Prata', None),
#     ('Kawasaki Z650', 2023, 48000.0, 'Azul', None),
#     ('Suzuki V-Strom 650', 2023, 69000.0, 'Cinza', None)
# ]
# cursor.executemany("INSERT INTO Moto (Modelo, Ano, Preco, Cor, IDCompra) VALUES (?, ?, ?, ?, ?)", moto_data)

# # Deletando clientes menores de idade

# Deletando clientes menores de idade


# try:
#     cursor.execute("DELETE from Clientes WHERE Idade < 18")
#     print("Os dados foram deletados com sucesso!")
# except sqlite3.Error as erro:
#     print("Erro ao deletar os dados:", erro)



# # Número de clientes menores de idade
# cursor.execute("SELECT COUNT(*) FROM Clientes WHERE Idade <= 18")
# num_clientes_maiores = cursor.fetchone()[0]
# print(f"Número de clientes menores de idade: {num_clientes_maiores}")


# Deletando uma moto pelo seu ID
# try:
#     moto_id_para_deletar = 3 ]
#     cursor.execute("DELETE FROM Moto WHERE IDMoto = ?", (moto_id_para_deletar,))
#     print("Moto deletada com sucesso!")
# except sqlite3.Error as erro:
#     print("Erro ao deletar a moto:", erro)

# Atualizando dados
# cursor.execute("UPDATE Clientes SET Idade = 35 WHERE Nome = 'Fernanda Lima'")
# cursor.execute("UPDATE Moto SET Preco = 45000.0 WHERE IDMoto = 2")


# Atualizando dados
# cursor.execute("UPDATE Clientes SET Idade = 35 WHERE Nome = 'Fernanda Lima'")



# Atualizando compra de moto
# try:
#     cursor.execute("UPDATE Moto SET IDCompra = ? WHERE IDMoto = ?", (11, 11))
#     print("Moto atualizada com sucesso!")
# except sqlite3.Error as erro:
#     print("Erro ao atualizar a moto:", erro)

# Commit das alterações
banco.commit()

# CONSULTAS

# # Clientes
# cursor = banco.execute("SELECT * FROM Clientes")
# print("Tabela Clientes:")
# for row in cursor:
#     print(row)


# # Consulta 
# cursor = banco.execute("SELECT * FROM Clientes")
# print("Tabela Clientes:")
# for row in cursor:
#     print(row)


# # Compras
# cursor = banco.execute("SELECT * FROM Compra")
# print("\nTabela Compra:")
# for row in cursor:
#     print(row)

# # Motos
# cursor = banco.execute("SELECT * FROM Moto")
# print("\nTabela Moto:")
# for row in cursor:
#     print(row)

# # Todas as compras feitas por um cliente específico
# cliente_id = 2  # ID do cliente desejado
# cursor.execute("SELECT * FROM Compra WHERE IDCliente = ?", (cliente_id,))
# for row in cursor:
#     print(row)

# # Valor total gasto por um cliente específico
# cliente_id = 3  
# cursor.execute("SELECT SUM(Valor) FROM Compra WHERE IDCliente = ?", (cliente_id,))
# total_gasto = cursor.fetchone()[0]
# print(f"Total gasto pelo cliente ID {cliente_id}: R${total_gasto:.2f}")

# # Encontrar a moto mais barata
# cursor.execute("SELECT * FROM Moto ORDER BY Preco DESC LIMIT 1")
# moto_mais_barata = cursor.fetchone()
# print("Moto mais barata:")
# print(moto_mais_barata)

# # Encontrar motos não compradas
# cursor.execute("SELECT * FROM Moto WHERE IDCompra IS NULL")
# motos_nao_compradas = cursor.fetchall()
# print("Motos que ainda não foram compradas:")
# for moto in motos_nao_compradas:
#     print(moto)

# Fechando a conexão
banco.close()
