import sqlite3

# Conectando ao banco de dados (será criado se não existir)
banco = sqlite3.connect('concessionaria.db')

# "Ponte" entre o python e o banco de dados, usado para executar comandos
cursor = banco.cursor()



# Criando a tabela de Clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                IDCliente INTEGER PRIMARY KEY,
                Nome TEXT NOT NULL,
                Idade INTEGER,
                Telefone TEXT,
                Email TEXT,
                Endereco TEXT
            );''')




# Inserindo dados na tabela de Clientes
clientes_data = [
    ('João Silva', 30,'111-1111', 'joao@gmail.com', 'Rua A, 123'),
    ('Maria Souza', 45,'222-2222', 'maria@gmail.com', 'Avenida B, 456'),
    ('Carlos Oliveira', 17,'333-3333', 'carlos@gmail.com', 'Rua X, 789'),
    ('Ana Rodrigues', 61,'777-8888', 'ana@gmail.com', 'Avenida Y, 101'),
    ('Paulo Santos', 25,'999-0000', 'paulo@gmail.com', 'Praça Z, 222'),
    ('Fernanda Lima', 34,'222-3333', 'fernanda@gmail.com', 'Estrada W, 333'),
]
cursor.executemany("INSERT INTO Clientes (Nome, Idade, Telefone, Email, Endereco) VALUES (?, ?, ?, ?, ?)",
                 clientes_data)




# Deletando clientes menores de idade
# try:
#     cursor.execute("DELETE from Clientes WHERE Idade < 18")
#     print("Os dados foram deletados com sucesso!")
# except sqlite3.Error as erro:
#     print("Erro ao deletar os dados:", erro)



# Atualizando dados
# cursor.execute("UPDATE Clientes SET Idade = 35 WHERE Nome = 'Fernanda Lima'")




# Commit das alterações
banco.commit()




# Consulta 
cursor = banco.execute("SELECT * FROM Clientes")
for row in cursor:
    print(row)




# Fechando a conexão
banco.close()
