import tkinter as tk
from tkinter import messagebox as mb
import sqlite3


connection=sqlite3.connect("acc.db")

cursor=connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (conta INTERGER, senha INTERGER, nome STR, cpf INTERGER, renda INTERGER, f STR)")
cursor.execute(f"INSERT INTO clientes VALUES (123, 123, 'Haroldo', 12332112332, 15000, 'adm')")
cursor.execute(f"INSERT INTO clientes VALUES (456, 456, 'Olivia', 235217563, 15000, 'c')")


cursor.execute("CREATE TABLE IF NOT EXISTS investimentos (nome TEXT, valor INTERGER)")
cursor.execute(f"INSERT INTO investimentos VALUES ('Apple', 129)")


def re_cliB(root, nomeCliente):
    cursor.execute(f"DELETE FROM clientes WHERE nome='{nomeCliente}'")
    connection.commit
    re_cli(root)



def re_cli(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text='')
    t1.pack()

    t2 = tk.Label(root, text='Remover Cliente')
    t2.pack()

    cursor.execute("SELECT nome FROM clientes")
    cliente=cursor.fetchall()

    for clientes in cliente:
        nomeCliente = clientes[0]
        b1=tk.Button(root, text=nomeCliente, command=lambda:re_cliB(root, nomeCliente))
        b1.pack()

    b2 = tk.Button(root, text="Voltar", command=lambda:tel_adm(root))
    b2.pack()





def re_invB(root, nomeInvestimento):
    cursor.execute(f"DELETE FROM investimentos WHERE nome='{nomeInvestimento}'")
    connection.commit
    re_inv(root)


def re_inv(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text='')
    t1.pack()

    t2 = tk.Label(root, text='Remover Investimento')
    t2.pack()

    cursor.execute("SELECT nome FROM investimentos")
    investimento=cursor.fetchall()

    for investimentos in investimento:
        nomeInvestimento = investimentos[0]
        b1=tk.Button(root, text=nomeInvestimento, command=lambda:re_invB(root, nomeInvestimento))
        b1.pack()

    b2 = tk.Button(root, text="Voltar", command=lambda:tel_adm(root))
    b2.pack()



def add_nc(e1, e2, e3, e4, e5):
    print('1')
    nome = e1.get()
    conta = e2.get()
    senha = e3.get()
    cpf = e4.get()
    renda = e5.get()
    cursor.execute(f"INSERT INTO clientes VALUES ({conta}, {senha}, '{nome}', {cpf}, {renda}, 'c')")
    connection.commit
    resultado = cursor.fetchone()
    mb.showinfo("Sucesso", f"A conta do cliente {nome} foi criada!")
    if resultado:
        print('Foi')
    else:
        print('Não foi')


def add_ni(e1, e2):
    print('teste')
    nome = e1.get()
    valor = e2.get()
    cursor.execute(f"INSERT INTO investimentos VALUES ('{nome}', {valor})")
    connection.commit
    mb.showinfo('Sucesso.', f'O investimento {nome} foi adicionado!')



def tela_ni(root):
    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()    
    
    t1 = tk.Label(root, text="Tela do Administrador")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t3 = tk.Label(root, text='Adicionar novo investimento')
    t3.pack

    t4 = tk.Label(root, text="Nome do Investimento")
    t4.pack()

    e1 = tk.Entry(root)
    e1.pack()

    t5 = tk.Label(root, text="Valor das Ações")
    t5.pack()

    e2 = tk.Entry(root)
    e2.pack()


    b1 = tk.Button(root, text="Adicionar Investimento", command=lambda:add_ni(e1, e2))
    b1.pack()

            
    b2 = tk.Button(root, text="Voltar", command=lambda:tel_adm(root))
    b2.pack()
    
    b3 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b3.pack()




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


    t7 = tk.Label(root, text="CPF")
    t7.pack()

    e4 = tk.Entry(root)
    e4.pack()

    t8 = tk.Label(root, text="Renda Mensal Média")
    t8.pack()

    e5 = tk.Entry(root)
    e5.pack()


    b1 = tk.Button(root, text="Adicionar Cliente", command=lambda:add_nc(e1, e2, e3, e4, e5))
    b1.pack()

        
    b2 = tk.Button(root, text="Voltar", command=lambda:tel_adm(root))
    b2.pack()

    
    b3 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b3.pack()


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

    b3 = tk.Button(root, text="Remover Investimento", command=lambda:re_inv(root))
    b3.pack()

    b4 = tk.Button(root, text="Remover Cliente", command=lambda:re_cli(root))
    b4.pack()

    b5 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b5.pack()



def tela_inv2(root, nomeInvestimento, nomeCliente, rendaCliente):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()

    t2 = tk.Label(root, text=f"Investimento {nomeInvestimento}")
    t2.pack()

    textoSlider = tk.StringVar()
    w1 = tk.Scale(root, from_=0, to=50, orient=tk.HORIZONTAL)
    w1["command"] = lambda x:textoSlider.set(w1.get())
    w1.pack()

    t1 = tk.Label(root, text="Seus lucros")
    t1.pack()

    b1 = tk.Button(root, text="Voltar", command=lambda:tela_inv(root, nomeCliente, rendaCliente))
    b1.pack()
    

        

def tela_inv(root, nomeCliente, rendaCliente):
    for widget in root.winfo_children():
        widget.destroy()
    
    t1 = tk.Label(root, text="Tela de Investimentos")
    t1.pack()

    cursor.execute("SELECT nome FROM investimentos")
    investimento=cursor.fetchall()

    for investimentos in investimento:
        nomeInvestimento = investimentos[0]
        b1=tk.Button(root, text=nomeInvestimento, command=lambda:tela_inv2(root, nomeInvestimento, nomeCliente, rendaCliente))
        b1.pack()

    t1 = tk.Label(root, text="Seus lucros")
    t1.pack()

    b3 = tk.Button(root, text="Voltar", command=lambda:tel_acc(root, nomeCliente, rendaCliente))
    b3.pack()





def tel_acc(root, nomeCliente, rendaCliente):
    print('2')
    for widget in root.winfo_children():
        widget.destroy()

    t2 = tk.Label(root, text="")
    t2.pack()    
    
    t1 = tk.Label(root, text="Sua conta")
    t1.pack()

    t2 = tk.Label(root, text="")
    t2.pack()

    t1 = tk.Label(root, text=f"Olá, {nomeCliente}, seja bem vindo!")
    t1.pack()


    b1 = tk.Button(root, text="Acessar seus investimentos", command=lambda:tela_inv(root, nomeCliente, rendaCliente))

    if rendaCliente < 15000:
        b1.config(state=tk.DISABLED)
    else:
        b1.config(state=tk.NORMAL)

    b1.pack()

    b2 = tk.Button(root, text="Voltar à tela inicial", command=lambda:login(root))
    b2.pack()



def entrar(e1, e2, login_fame, root):
    print('1')
    conta = e1.get()
    senha = e2.get()
    cursor.execute(f"SELECT nome, renda, f FROM clientes WHERE(conta={conta} AND senha={senha})")
    resultado = cursor.fetchone()
    if resultado:
        nomeCliente = resultado[0]
        rendaCliente = resultado[1]
        função = resultado[2]
        if função == 'adm':
            tel_adm(root)
        else:
            print('Foi')
            login_fame.pack_forget
            tel_acc(root, nomeCliente, rendaCliente)
    else:
        print('Não foi')
        mb.showinfo('Erro', 'Conta ou senha incorretos.')

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