import sqlite3 as sql


# Classe do Banco de Dados
class Database(): 
    database= "alunos.db"
    conn= None
    cur= None
    connected= False

# Função para conectar com o Banco de Dados
    def connect(self): 
        Database.conn = sql.connect(Database.database)
        Database.cur = Database.conn.cursor()
        Database.connected = True

# Função para encerrar a conexão com o Banco de Dados
    def disconnect(self): 
        Database.conn.close()
        Database.connected = False

# Função para executar um comando no Banco de Dados
    def execute(self, sql, parms = None): 
        if Database.connected:
            if parms == None:
                Database.cur.execute(sql)
            else:
                Database.cur.execute(sql, parms)
            return True
        else:
            return False

# Função para recuperar os valores recebidos
    def fetchall(self): 
        return Database.cur.fetchall()

# Função para gravar os dados inseridos
    def save(self): 
        if Database.connected:
            Database.conn.commit()
            return True
        else:
            return False

# Função para conectar ao Banco de Dados e criar tabela de Alunos 
def startDB(): 
    trans = Database()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY , nome TEXT, cpf TEXT)")
    trans.save()
    trans.disconnect()

# INTERAÇÃO COM A INTERFACE GRÁFICA

# Função para listar os dados
def list(): 
    trans = Database()
    trans.connect()
    trans.execute("SELECT * FROM alunos") 
    rows = trans.fetchall()
    trans.disconnect()
    return rows 

# Função para cadastrar os dados
def insert(nome, cpf): 
    trans = Database()
    trans.connect()
    trans.execute("INSERT INTO alunos VALUES(NULL, ?,?)", (nome, cpf))
    trans.save()
    trans.disconnect()

# Função para buscar os dados
def search(nome="", cpf=""): 
    trans = Database()
    trans.connect()
    trans.execute("SELECT * FROM alunos WHERE nome=? or cpf=?", (nome, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Função para apagar os dados
def delete(id):
    trans = Database()
    trans.connect()
    trans.execute("DELETE FROM alunos WHERE id = ?", (id,))
    trans.save()
    trans.disconnect()

# Função para atualizar os dados
def update(id, nome, cpf):
    trans = Database()
    trans.connect()
    trans.execute("UPDATE alunos SET nome =?, cpf=? WHERE id = ?",(nome, cpf, id))
    trans.save()
    trans.disconnect()

startDB()
