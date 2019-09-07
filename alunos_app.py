# Importando o arquivo de Interface Gráfica

from alunos_gui import *
import alunos_db 

app = None

# Função para visualizar os alunos cadastrados
def list(): 
    rows = alunos_db.list()
    app.listAlunos.delete(0, END)
    for r in rows:
        app.listAlunos.insert(END, r)

# Função para buscar os alunos cadastrados
def search(): 
    app.listALunos.delete(0, END)
    rows = alunos_db.search(app.txtNome.get(), app.txtCPF.get()) 
    for r in rows:
        app.listAlunos.insert(END, r)

# Função para inserir dados dos alunos
def insert():
    alunos_db.insert(app.txtNome.get(), app.txtCPF.get()) 
    list() 

# Função para atualizar os dados dos alunos cadastrados
def update():
    alunos_db.update(selected[0],app.txtNome.get(), app.txtCPF.get())
    list() 

# Função para apagar os dados dos alunos cadastrados
def delete():
    id = selected[0]
    alunos_db.delete(id)
    list() 

# Função para receber os dados da lista (alunos cadastrados) e preencher nos campos
def getSelectedRow(event):  
    global selected
    index = app.listAlunos.curselection()[0] 
    selected = app.listAlunos.get(index) 
    app.entNome.delete(0, END) 
    app.entNome.insert(END, selected[1])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[2])

    return selected

# Associando os comandos do App à Interface Gráfica

if __name__ == "__main__":
    app = Gui()
    app.listAlunos.bind('<<ListboxSelect>>', getSelectedRow) 
    
    app.btnInserir.configure(command=insert)
    app.btnAtualizar.configure(command=update)
    app.btnListar.configure(command=list)
    app.btnApagar.configure(command=delete)
    app.run() 
