import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


connection=sqlite3.connect("acc.db")

cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (conta INTERGER, senha INTERGER, nome STR, cpf INTERGER)")

cursor.execute(f"INSERT INTO clientes VALUES (123, 123)")

def add_nc(e1, e2, e3):
    print('1')
    nome = e1.get()
    conta = e2.get()
    senha = e3.get()
    cursor.execute(f"INSERT INTO clientes VALUES ({conta}, {senha})")
    connection.commit
    resultado = cursor.fetchone()
    mb.showinfo("Sucesso", f"A conta do cliente {nome} foi criada!")
    if resultado:
        print('Foi')
    else:
        print('Não foi')


def tela_nc(root):
    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()    
    
    t1 = tk.Label(root, text="Tela do Administrador")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t3 = tk.Label(root, text='Adicionar novo cliente')
    t3.pack

    t4 = tk.Label(root, text="Nome do Cliente")
    t4.pack()

    e1 = tk.Entry(root)
    e1.pack()

    t5 = tk.Label(root, text="Número da Conta")
    t5.pack()

    e2 = tk.Entry(root)
    e2.pack()

    t6 = tk.Label(root, text="Senha")
    t6.pack()

    e3 = tk.Entry(root)
    e3.pack()

    b1 = tk.Button(root, text="Adicionar Cliente", command=lambda:add_nc(e1, e2, e3))
    b1.pack()

    
    b2 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b2.pack()


def tel_adm(root):
    print('2')
    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()    
    
    t1 = tk.Label(root, text="Tela do Administrador")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t1 = tk.Label(root, text="Olá, seja bem vindo!")
    t1.pack()


    b1 = tk.Button(root, text="Adicionar Investimento", command=lambda:tela_ni(root))
    b1.pack()

    b2 = tk.Button(root, text="Adicionar Novo Cliente", command=lambda:tela_nc(root))
    b2.pack()


    b3 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b3.pack()





def tela_ms(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()

    t2 = tk.Label(root, text="Investimento na Microsoft")
    t2.pack()

    textoSlider = tk.StringVar()
    w1 = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL)
    w1["command"] = lambda x:textoSlider.set(w1.get())
    w1.pack()

    t1 = tk.Label(root, text="Seus lucros")
    t1.pack()

    b1 = tk.Button(root, text="Voltar", command=lambda:tela_inv(root))
    b1.pack()

    
    b1 = tk.Button(root, text="a", command=lambda:tel_adm(root))
    b1.pack()
    




def tela_apple(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()

    t2 = tk.Label(root, text="Investimento na Apple")
    t2.pack()

    textoSlider = tk.StringVar()
    w1 = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL)
    w1["command"] = lambda x:textoSlider.set(w1.get())
    w1.pack()

    t1 = tk.Label(root, text="Seus lucros")
    t1.pack()

    b1 = tk.Button(root, text="Voltar", command=lambda:tela_inv(root))
    b1.pack()
    

        

def tela_inv(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()

    b1 = tk.Button(root, text="Investimento na Apple", command=lambda:tela_apple(root))
    b1.pack()

    b2 = tk.Button(root, text="Investimento na Microsoft", command=lambda:tela_ms(root))
    b2.pack()

    t1 = tk.Label(root, text="Seus lucros")
    t1.pack()

    b3 = tk.Button(root, text="Voltar", command=lambda:tel_acc(root))
    b3.pack()
    





def tel_acc(root):
    print('2')
    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()    
    
    t1 = tk.Label(root, text="Sua conta")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t1 = tk.Label(root, text="Olá, seja bem vindo!")
    t1.pack()


    b1 = tk.Button(root, text="Acessar seus investimentos", command=lambda:tela_inv(root))
    b1.pack()

    b2 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b2.pack()



def entrar(e1, e2, login_fame, root):
    print('1')
    conta = e1.get()
    senha = e2.get()
    cursor.execute(f"SELECT * FROM clientes WHERE(conta={conta} AND senha={senha})")
    resultado = cursor.fetchone()
    if resultado:
        print('Foi')
        login_fame.pack_forget
        tel_acc(root)
    else:
        print('Não foi')

def login(root):        

    login_frame = tk.Frame(root)

    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()

    t1 = tk.Label(root, text="Tela de Login")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t2 = tk.Label(root, text="Conta")
    t2.pack()

    e1 = tk.Entry(root)
    e1.pack()

    t2 = tk.Label(root, text="Senha")
    t2.pack()

    e2 = tk.Entry(root, show="*")
    e2.pack()

    t2 = tk.Label(root, text="")
    t2.pack()
    
    b1 = tk.Button(root, text="Entrar", command=lambda:entrar(e1, e2, login_frame, root))
    b1.pack()

    exit = tk.Button(root, text="Sair", command=root.destroy)
    exit.pack()





def main():
    root = tk.Tk()
    root.title("Banco Invest")
    root.resizable(True, True)
        
    login(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop() 