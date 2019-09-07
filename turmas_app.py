# Importando o arquivo de Interface Gráfica

from turmas_gui import *
import turmas_db


app = None

# Função para visualizar as turmas cadastradas
def list(): 
    rows = turmas_db.list()
    app.listTurmas.delete(0, END)
    for r in rows:
        app.listTurmas.insert(END, r)

# Função para buscar as turmas cadastradas
def search(): 
    app.listTurmas.delete(0, END)
    rows = turmas_db.search(app.txtCod.get(), app.txtPeriodo.get(), app.txtCodis.get(), app.txtCpfprof.get(), app.txtCpfAlun.get()) #chamando a função buscar do banco, e pegando as informações das variáveis que estão com o entry
    for r in rows:
        app.listTurmas.insert(END, r)

# Função para inserir os dados das turmas cadastradas
def insert():
    turmas_db.insert(app.txtCod.get(), app.txtPeriodo.get(), app.txtCodis.get(), app.txtCpfprof.get(), app.txtCpfAlun.get()) #pega a entrada dos usuários
    list()

# Função para atualizar os dados das turmas cadastradas
def update():
    turmas_db.update(selected[0],app.txtCod.get(), app.txtPeriodo.get(), app.txtCodis.get(), app.txtCpfprof.get(), app.txtCpfAlun.get())
    list() 

# Função para apagar os dados das turmas cadastradas
def delete():
    id = selected[0]
    turmas_db.delete(id)
    list() 

# Função para receber os dados da lista (tumras cadastradas) e preencher nos campos
def getSelectedRow(event): 
    global selected
    index = app.listTurmas.curselection()[0]
    selected = app.listTurmas.get(index) 
    app.entCod.delete(0, END) 
    app.entCod.insert(END, selected[1])
    app.entPeriodo.delete(0, END)
    app.entPeriodo.insert(END, selected[2])
    app.entCodis.delete(0, END)
    app.entCodis.insert(END, selected[3])
    app.entCPFprof.delete(0, END)
    app.entCPFprof.insert(END, selected[4])
    app.entCPFalun.delete(0, END)
    app.entCPFalun.insert(END, selected[5])

    return selected

# Associando os comandos do App à Interface Gráfica

if __name__ == "__main__":
    app = Gui()
    app.listTurmas.bind('<<ListboxSelect>>', getSelectedRow) 
    
    app.btnInserir.configure(command=insert)
    app.btnAtualizar.configure(command=update)
    app.btnListar.configure(command=list)
    app.btnApagar.configure(command=delete)
    app.run() 
