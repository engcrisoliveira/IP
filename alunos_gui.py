# Importando a biblioteca Tkinter e ttk

from tkinter import *

# Função para definir a Interface Gráfica

class Gui():

    # Janela da Interface Gráfica
    window = Tk()
    window.title("ALUNOS")
        
    # Variáveis que armazenam o texto inserido no campo de entrada
    txtNome= StringVar() 
    txtCPF= StringVar()
  
    # Itens da janela da Interface Gráfica
    lblnome= Label(window, text="NOME") 
    lblcpf= Label(window, text="CPF") 
    entNome= Entry(window, textvariable=txtNome, width=20) 
    entCPF= Entry(window, textvariable=txtCPF, width=20) 
    listAlunos= Listbox(window, width=100) 
    scrollAlunos = Scrollbar(window)
    
    # Botões da janela da Interface Gráfica
    btnInserir= Button(window, text="INSERIR")
    btnAtualizar= Button(window, text="ATUALIZAR")
    btnListar= Button(window, text="LISTAR")
    btnApagar= Button(window, text="APAGAR")
   
    # Posição dos elementos nas janelas da Interface Gráfica
    lblnome.grid(row=0,column=0) 
    lblcpf.grid(row=1, column=0) 
    entNome.grid(row=0, column=1, padx=50, pady=50) 
    entCPF.grid(row=1, column=1) 
    listAlunos.grid(row=0, column=2, rowspan=10) 
    scrollAlunos.grid(row=0, column=6, rowspan=10)  
    btnInserir.grid(row=2, column=0, columnspan=2)
    btnAtualizar.grid(row=3, column=0, columnspan=2)
    btnListar.grid(row=4, column=0, columnspan=2)
    btnApagar.grid(row=5, column=0, columnspan=2)
    
    # Juntando a barra de rolagem com a lista de alunos
    listAlunos.configure(yscrollcommand=scrollAlunos.set) 
    scrollAlunos.configure(command=listAlunos.yview) 

    # Definindo a largura e o posicionamento dos widgets
    for child in window.winfo_children(): 
        widget_class = child.__class__.__name__ 
        if widget_class == "Button": 
            child.grid_configure(sticky='WE', padx=4, pady=2) 
        elif widget_class == "Listbox": 
            child.grid_configure(padx=4, pady=2, sticky='NS')
        elif widget_class == "Scrollbar": 
            child.grid_configure(padx=4, pady=2, sticky='NS')
        else:
            child.grid_configure(padx=4, pady=2, sticky='N')

    def run(self): 
        Gui.window.mainloop() 
