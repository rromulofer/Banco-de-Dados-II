import sqlite3

# Conectando ao banco de dados (será criado se não existir)
banco = sqlite3.connect('concessionaria.db')

cursor = banco.cursor()

# Criando a tabela de Clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                IDCliente INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Telefone TEXT,
                Email TEXT,
                Endereco TEXT
            );''')

# Inserindo dados na tabela de Clientes
clientes_data = [
    ('João Silva', '123-4567', 'joao@example.com', 'Rua A, 123'),
    ('Maria Souza', '987-6543', 'maria@example.com', 'Avenida B, 456')
]
cursor.executemany("INSERT INTO Clientes (Nome, Telefone, Email, Endereco) VALUES (?, ?, ?, ?)",
                 clientes_data)

# Commit das alterações
banco.commit()

# Realizando uma consulta simples
cursor = banco.execute("SELECT * FROM Clientes")
for row in cursor:
    print(row)

# Fechando a conexão
banco.close()
