# Importando o arquivo de Interface Gráfica

from professores_gui import *
import professores_db 

app = None

# Função para visualizar os professores cadastrados
def list(): 
    rows = professores_db.list()
    app.listProfessores.delete(0, END)
    for r in rows:
        app.listProfessores.insert(END, r)

# Função para buscar os professores cadastrados
def search(): 
    app.listProfessores.delete(0, END)
    rows = professores_db.sea(app.txtNome.get(), app.txtCPF.get(), app.txtDep.get()) #chamando a função buscar do banco, e pegando as informações das variáveis que estão com o entry
    for r in rows:
        app.listProfessores.insert(END, r)

# Função para inserir dados dos professores
def insert():
    professores_db.insert(app.txtNome.get(), app.txtCPF.get(), app.txtDep.get()) #pega a entrada dos usuários
    list() 

# Função para atualizar dados dos professores
def update():
    professores_db.update(selected[0],app.txtNome.get(), app.txtCPF.get(), app.txtDep.get())
    list() 

# Função para apagar dados dos professores
def delete():
    id = selected[0]
    professores_db.delete(id)
    list() 


# Função para receber os dados da lista (professores cadastrados) e preencher nos campos
def getSelectedRow(event): 
    global selected
    index = app.listProfessores.curselection()[0] 
    selected = app.listProfessores.get(index) 
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[2])
    app.entDep.delete(0, END)
    app.entDep.insert(END, selected[3])

    return selected

# Associando os comandos do App à Interface Gráfica
if __name__ == "__main__":
    app = Gui()
    app.listProfessores.bind('<<ListboxSelect>>', getSelectedRow) 
    
    app.btnInserir.configure(command=insert)
    app.btnAtualizar.configure(command=update)
    app.btnListar.configure(command=list)
    app.btnApagar.configure(command=delete)
    app.run() 
