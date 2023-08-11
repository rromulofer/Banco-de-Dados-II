import sqlite3

# Conectar-se ao banco de dados (será criado se não existir)
conn = sqlite3.connect('concessionaria2.db')

# Criar a tabela de Clientes
conn.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                IDCliente INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Telefone TEXT,
                Email TEXT,
                Endereco TEXT
            );''')

# Inserir dados na tabela de Clientes
clientes_data = [
    ('João Silva', '123-4567', 'joao@example.com', 'Rua A, 123'),
    ('Maria Souza', '987-6543', 'maria@example.com', 'Avenida B, 456')
]
conn.executemany("INSERT INTO Clientes (Nome, Telefone, Email, Endereco) VALUES (?, ?, ?, ?)",
                 clientes_data)

# Realizar uma consulta simples
cursor = conn.execute("SELECT * FROM Clientes")
for row in cursor:
    print(row)

# Commit das alterações
conn.commit()

# Fechar a conexão
conn.close()
