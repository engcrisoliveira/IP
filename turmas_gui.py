# Importando a biblioteca Tkinter e ttk

from tkinter import *

# Função para definir a Interface Gráfica

class Gui(): 
    window = Tk() 
    window.title("TURMAS") 

    # Variáveis que armazenam o texto inserido no campo de entrada
    txtCod = StringVar()
    txtPeriodo= StringVar()
    txtCodis= StringVar()
    txtCpfprof= StringVar()
    txtCpfAlun= StringVar()

    # Itens da janela da Interface Gráfica
    lblcod = Label(window, text="CÓDIGO DA TURMA")
    lblperiodo = Label(window, text="PERÍODO") 
    lblcodis = Label(window, text="CÓDIGO DA DISCIPLINA")
    lblcpfprof = Label(window, text="CPF DO PROFESSOR")
    lblcpfalun = Label(window, text="CPF DO ALUNO")
    entCod = Entry(window, textvariable=txtCod, width=20) 
    entPeriodo = Entry(window, textvariable=txtPeriodo, width=20)
    entCodis = Entry(window, textvariable=txtCodis, width=20)
    entCPFprof = Entry(window, textvariable=txtCpfprof, width=20)
    entCPFalun = Entry(window, textvariable=txtCpfAlun, width=20)
    listTurmas = Listbox(window, width=100) 
    scrollTurmas = Scrollbar(window) 

    # Botões da janela da Interface Gráfica
    btnInserir= Button(window, text="INSERIR")
    btnAtualizar= Button(window, text="ATUALIZAR")
    btnListar= Button(window, text="LISTAR")
    btnApagar= Button(window, text="APAGAR")
    
    # Posição dos elementos nas janelas da Interface Gráfica
    lblcod.grid(row=0, column=0)
    lblperiodo.grid(row=1, column=0)
    lblcodis.grid(row=2, column=0)
    lblcpfprof.grid(row=3, column=0)
    lblcpfalun.grid(row=4, column=0)
    entCod.grid(row=0, column=1, padx=5, pady=5)
    entPeriodo.grid(row=1, column=1)
    entCodis.grid(row=2, column=1)
    entCPFprof.grid(row=3, column=1)
    entCPFalun.grid(row=4, column=1)
    listTurmas.grid(row=0, column=2, rowspan=10)
    scrollTurmas.grid(row=0, column=6, rowspan=10)
    
    btnInserir.grid(row=5, column=0, columnspan=2)
    btnAtualizar.grid(row=6, column=0, columnspan=2)
    btnListar.grid(row=7, column=0, columnspan=2)
    btnApagar.grid(row=8, column=0, columnspan=2)
    
    # Juntando a barra de rolagem com a lista de alunos
    listTurmas.configure(yscrollcommand=scrollTurmas.set)
    scrollTurmas.configure(command=listTurmas.yview)
    
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
