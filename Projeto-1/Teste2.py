import sqlite3

def conectar_banco(nome_banco):
    return sqlite3.connect(nome_banco)

def criar_tabela_clientes(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            IDCliente INTEGER PRIMARY KEY,
            Nome TEXT NOT NULL,
            Telefone TEXT,
            Email TEXT,
            Endereco TEXT
        );
    ''')
    conexao.commit()

def inserir_cliente(conexao, nome, telefone, email, endereco):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO Clientes (Nome, Telefone, Email, Endereco)
        VALUES (?, ?, ?, ?);
    ''', (nome, telefone, email, endereco))
    conexao.commit()

def listar_clientes(conexao):
    cursor = conexao.execute('SELECT * FROM Clientes')
    return cursor.fetchall()

def atualizar_cliente(conexao, id_cliente, novo_nome):
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE Clientes
        SET Nome = ?
        WHERE IDCliente = ?;
    ''', (novo_nome, id_cliente))
    conexao.commit()

def excluir_cliente(conexao, id_cliente):
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM Clientes
        WHERE IDCliente = ?;
    ''', (id_cliente,))
    conexao.commit()

# Exemplo de uso das funções
banco = conectar_banco('concessionaria.db')

criar_tabela_clientes(banco)

# Inserindo um cliente
inserir_cliente(banco, 'João Silva', '123-4567', 'joao@example.com', 'Rua A, 123')

# Listando clientes
clientes = listar_clientes(banco)
for cliente in clientes:
    print(cliente)

# Atualizando um cliente
atualizar_cliente(banco, 1, 'João da Silva')

# Excluindo um cliente
excluir_cliente(banco, 2)

banco.close()
