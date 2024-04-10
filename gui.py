import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


connection=sqlite3.connect("acc.db")

cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (conta INTERGER, senha INTERGER, nome STR, cpf INTERGER)")

cursor.execute(f"INSERT INTO clientes VALUES (123, 123)")





        

def tela_inv(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()
    





def tel_acc(root):
    print('2')
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Sua conta")
    t1.pack()


    b1 = tk.Button(root, text="Acessar seus investimentos", command=lambda:tela_inv(root))
    b1.pack()

    b2 = tk.Button(root, text="Voltar à tela inicial", command=login(root))
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



    t1 = tk.Label(root, text="Tela de Login")
    t1.pack()

    t2 = tk.Label(root, text="Conta")
    t2.pack()

    e1 = tk.Entry(root)
    e1.pack()

    t2 = tk.Label(root, text="Senha")
    t2.pack()

    e2 = tk.Entry(root, show="*")
    e2.pack()
    
    b1 = tk.Button(root, text="Entrar", command=lambda:entrar(e1, e2, login_frame, root))
    b1.pack()





def principal():
    root = tk.Tk()
    root.title("Banco Invest")
    root.resizable(True, True)
        
    login(root)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop() 



principal()