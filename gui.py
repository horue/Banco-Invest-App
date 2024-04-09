import tkinter as tk
import sqlite3


connection=sqlite3.connect("acc.db")

cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (conta INTERGER, senha INTERGER)")

cursor.execute(f"INSERT INTO clientes VALUES (123, 123)")




def entrar(e1, e2):
    print('1')
    conta = e1.get(e1)
    senha = e2.get(e2)
    cursor.execute(f"SELECT * FROM clientes WHERE(conta={conta} AND senha={senha}")
    resultado = cursor.fetchone()
    if resultado:
        print('Foi')
    else:
        print('Não foi kkj')



def principal():
    root = tk.Tk()
    root.title("Banco Invest")
    root.resizable(True, True)
        
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
    
    b1 = tk.Button(root, text="Entrar", command=entrar)
    b1.pack()






    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop() 

principal()