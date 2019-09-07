import sqlite3 as sql


# Classe do Banco de Dados
class Database(): 
    database= "disciplinas.db"
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

# Função para conectar ao Banco de Dados e criar tabela de Disciplinas 
def startDB(): 
    trans = Database()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS disciplinas (id INTEGER PRIMARY KEY , nome TEXT, código TEXT)")
    trans.save()
    trans.disconnect()

# INTERAÇÃO COM A INTERFACE GRÁFICA

# Função para listar os dados
def list(): 
    trans = Database()
    trans.connect()
    trans.execute("SELECT * FROM disciplinas") 
    rows = trans.fetchall()
    trans.disconnect()
    return rows 

# Função para cadastrar os dados
def insert(nome, código): 
    trans = Database()
    trans.connect()
    trans.execute("INSERT INTO disciplinas VALUES(NULL, ?,?)", (nome, código))
    trans.save()
    trans.disconnect()

# Função para buscar os dados
def search(nome="", código=""): 
    trans = Database()
    trans.connect()
    trans.execute("SELECT * FROM disciplinas WHERE nome=? or código=?", (nome, código))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# Função para apagar os dados
def delete(id):
    trans = Database()
    trans.connect()
    trans.execute("DELETE FROM disciplinas WHERE id = ?", (id,))
    trans.save()
    trans.disconnect()

# Função para atualizar os dados
def update(id, nome, código):
    trans = Database()
    trans.connect()
    trans.execute("UPDATE disciplinas SET nome =?, código=? WHERE id = ?",(nome, código, id))
    trans.save()
    trans.disconnect()

startDB()
