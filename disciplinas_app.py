# Importando o arquivo de Interface Gráfica

from disciplinas_gui import *
import disciplinas_db

app = None

# Função para visualizar das disciplinas cadastradas
def list(): 
    rows = disciplinas_db.list()
    app.listDisciplinas.delete(0, END)
    for r in rows:
        app.listDisciplinas.insert(END, r)

# Função para buscar as disciplinas cadastradas
def search(): 
    app.listDisciplinas.delete(0, END)
    rows = Disciplinas_db.search(app.txtNome.get(), app.txtCódigo.get()) 
    for r in rows:
        app.listDisciplinas.insert(END, r)

# Função para inserir dados das disciplinas
def insert():
    disciplinas_db.insert(app.txtNome.get(), app.txtCódigo.get()) 
    list() 

# Função para atualizar os dados das disciplinas cadastradas
def update():
    disciplinas_db.update(selected[0],app.txtNome.get(), app.txtCódigo.get())
    list() 

# Função para apagar os dados das disciplinas cadastradas
def delete():
    id = selected[0]
    disciplinas_db.delete(id)
    list() 

# Função para receber os dados da lista (disciplinas cadastradas) e preencher nos campos
def getSelectedRow(event):  
    global selected
    index = app.listDisciplinas.curselection()[0] 
    selected = app.listDisciplinas.get(index) 
    app.entNome.delete(0, END) 
    app.entNome.insert(END, selected[1])
    app.entCódigo.delete(0, END)
    app.entCódigo.insert(END, selected[2])

    return selected

# Associando os comandos do App à Interface Gráfica

if __name__ == "__main__":
    app = Gui()
    app.listDisciplinas.bind('<<ListboxSelect>>', getSelectedRow) 
    
    app.btnInserir.configure(command=insert)
    app.btnAtualizar.configure(command=update)
    app.btnListar.configure(command=list)
    app.btnApagar.configure(command=delete)
    app.run() 
