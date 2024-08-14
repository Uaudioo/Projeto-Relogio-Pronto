import os
from tkinter import *
import random
import threading
from datetime import datetime as dt



#Config  Básica da tela.
window = Tk()
window.title("")
window.geometry("300x300")
window.config(bg="Gray")
window.resizable(width=False,height=False)

#Variaveis.
global data
global parar

parar = True

data = dt.now()



#Funções.
def atualizar_hora():
    # Atualiza a data e hora
    global data
    data = dt.now()
    # Formata a hora como string
    hora_formatada = data.strftime("%H:%M:%S")
    # Atualiza o texto do label
    label_data.config(text=hora_formatada)

    # Agenda a próxima atualização após 1000 milissegundos (1 segundo)

    window.after(1000, atualizar_hora)


def atualizar_data():

    global data

    data_formatada = data.strftime("%d/%m/%y")

    label_dias.config(text=data_formatada)
    
    window.after(1000, atualizar_data)

def fun_sair():
    
    global parar

    parar == True


    



#Labels.

label_data = Label(window,text = "",width = 10,height = 2,bg = "Black",fg = "White",relief = "raised")
label_data.grid(row=0,column=0,padx=3,pady=3)


label_dias = Label(window,text = "",width = 10,height = 2,bg = "Black",fg = "White",relief = "raised")
label_dias.grid(row=2,column=0,padx=3,pady=3)




#Botões.
ativar_data = Button (window,command= atualizar_hora,width=10,height=2,text="Mostrar Hora",bg="green")
ativar_data.grid(row=0,column=3,padx=3,pady=3)

ativar_dias = Button (window,command= atualizar_data,width=10,height=2,text="Mostrar Data",bg="green")
ativar_dias.grid(row=2,column=3,padx=3,pady=3)


ativar_sair = Button (window,command= fun_sair,width=10,height=2,text="Sair",bg="red")
ativar_sair.grid(row=4,column=3,padx=3,pady=3)





window.mainloop()