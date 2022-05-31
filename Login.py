from ast import Num, Pass
import random
from cProfile import label
from cgi import test
from cgitb import text
from email import message
from os import access
from ssl import VerifyFlags
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.tix import ButtonBox
from tokenize import Number
from turtle import left, title, width
from tkinter import ttk
from typing_extensions import Self
from django.db import DatabaseError
from pyrsistent import b
from setuptools import Command
from zmq import EVENT_LISTENING
import DataBaser
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

#---------------------------Funções--------------------------------





def LoginHome():
    LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=Login)
    LoginButton.place(x=150, y=225)

    RegisterButton = ttk.Button(RightFrame, text="Register", width=10, command=Register)
    RegisterButton.place(x=230, y=225)

    UserLabel = Label(RightFrame, text='Username:', font=('Century Gothic', 20), bg='#363636', fg='white')
    UserLabel.place(x=5, y=100)

    UserEntry = ttk.Entry(RightFrame, width=30)
    UserEntry.place(x=150, y=113)

    PassLabel = Label(RightFrame, text='Password:', font=('Century Gothic', 20), bg='#363636', fg='white')
    PassLabel.place(x=5, y=140)

    PassEntry = ttk.Entry(RightFrame, width=30, show='*')
    PassEntry.place(x=150, y=150)

    RecoverPassword = ttk.Button(RightFrame, text='Recover Pass', width =20, command=Recover)
    RecoverPassword.place(x=160, y=255) 



        

def Recover():

    PassLabel.place(x=5000)
    PassEntry.place(x=5000)
    PassLabel.place(x=5000)
    LoginButton.place(x=5000)
    RecoverPassword.place(x=5000)

    NumberLabel = Label(RightFrame, text='Número:', font=('Century Gothic', 20), bg="#363636", fg='white')
    NumberLabel.place(x=5, y=140)

    NumberEntry = ttk.Entry(RightFrame, width=30)
    NumberEntry.place(x = 150, y=150)
    
    #RequestButton = ttk.Button(RightFrame, text="Request", width=10)
    #RequestButton.place(x=190, y=255)

    

    BotCod = ttk.Button(RightFrame, text="Back", width=10, command=LoginHome)
    BotCod.place(x=150, y=225)

    def Recuperar():
        User = UserEntry.get()
        Number = int(NumberEntry.get())
        DataBaser.cursor.execute("""
        SELECT * FROM Users
        WHERE (User = ? AND Number = ?)
        """, (User, Number))
        print('Selecionou')
        verifyLogin = DataBaser.cursor.fetchone()
        try:
            (User in verifyLogin and Number in verifyLogin)

            messagebox.showinfo(title='Login Info', message="Digite o Código enviado para seu celular")
            codigo = random.randint(1000,4999)
            print(codigo)
            # Your Account SID from twilio.com/console
            account_sid = "ACba4b3587a386ca1e60cfde956be07b3b"
            # Your Auth Token from twilio.com/console
            auth_token  = "b29f4a9477f3bcf42fe40edf8622fadc"

            client = Client(account_sid, auth_token)



            try:
                # This could potentially throw an exception!
                message = client.messages.create(
                to="+55{}".format(int(Number)), 
                from_="+13184148720",
                body="Seu Código é: {}".format(codigo))

                #if codigo == 
            except TwilioRestException as err:
                # Implement your fallback code here
                print(err)
    
                
            UserEntry.place(x=5000)
            NumberEntry.place(x=5000)
            NumberLabel.place(x=5000)
            UserLabel.place(x=5000)
            RegisterButton.place(x=5000)
            RecoverPassword.place(x=5000)
            BotCod.place(x=5000)
            RecuperarPass.place(x=5000)

            def Codigoenviado():
                x = int(CodigoEntry.get())
                print(x)
                
                
                if x == codigo:
                    print('oie')
                    messagebox.showinfo(title='Login Info', message="Codigo Válido")
                    janela2()

                else:
                    print('deu ruim')
                    messagebox.showerror(title='Login Info', message="Codigo Invalido")
                    

                    
            CodigoLabel = Label(RightFrame, text='Código:', font=('Century Gothic', 20), bg="#363636", fg='white')
            CodigoLabel.place(x=5, y=140)

            CodigoEntry = ttk.Entry(RightFrame, width=30)
            CodigoEntry.place(x = 150, y=150)

            EnviarCodigo = ttk.Button(RightFrame, text='Enviar Codigo', width =20, command=Codigoenviado)
            EnviarCodigo.place(x=160, y=255)


        

                    
        except:
                    messagebox.showerror(title='Login Info', message="Acesso Negado")

    
    RecuperarPass = ttk.Button(RightFrame, text='Enviar', width =20, command=Recuperar)
    RecuperarPass.place(x=160, y=255)
        
    

        

    


    #Parei aqui, adicionar botoes ao revoer

    #print('Ola, mundo')


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (User, Pass))
    print('Selecionou')
    verifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in verifyLogin and Pass in verifyLogin):

            messagebox.showinfo(title='Login Info', message="Acesso Confirmado. Bem vindo!")
            
         
    except:
            messagebox.showerror(title='Login Info', message="Acesso Negado")

def Register():
    #Removendo Widgets de Login:
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #inserindo Widgets do Cadastro
    NomeLabel = Label(RightFrame, text='Name:', font=('Century Gothic', 20), bg="#363636", fg='white')
    NomeLabel.place(x=5, y=20)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=150, y=35)

    EmailLabel = Label(RightFrame, text='E-mail:', font=('Century Gothic', 20), bg='#363636', fg='white')
    EmailLabel.place(x=5, y=59)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x = 150, y=75)

    NumberLabel = Label(RightFrame, text='Número:', font=('Century Gothic', 20), bg="#363636", fg='white')
    NumberLabel.place(x=5, y=182)

    NumberEntry = ttk.Entry(RightFrame, width=30)
    NumberEntry.place(x = 150, y=190)

    RecoverPassword.place(x=5000)

    
    def RegisterToDataBase():
        
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        Number = NumberEntry.get()
        

        if (Name == "" or Email == "" or User == "" or Pass == "" or Number ==""):
            messagebox.showerror(title='Register Erro', message="Preencha todos os campos")
        elif Name == "":
            messagebox.showerror(title='Register Erro', message='Preencha todos os campos')
        elif Email == "":
            messagebox.showerror(title='Register Erro', message='Preencha todos os campos')
        elif User == "":
            messagebox.showerror(title='Register Erro', message='Preencha todos os campos')
        elif Pass == "":
            messagebox.showerror(title='Register Erro', message='Preencha todos os campos')
        elif Number == "":
            messagebox.showerror(title='Register Erro', message='Preencha todos os campos')

        elif '@' not in Email and '.com' not in Email:
            messagebox.showerror(title='Register Erro', message='Formato de Email inválido')
    
        else:
            try:
                DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password, Number) VALUES (?, ?, ?, ?, ?)
            
                """, (Name, Email, User, Pass, Number ))
                DataBaser.conn.commit()
                messagebox.showinfo(title='Register Info', message='Conta criada com Sucesso!')
            except:
                messagebox.showerror(title='Register Erro', message='Username já cadastrado!')

    
    Register = ttk.Button(RightFrame, text="Register", width=10, command=RegisterToDataBase)
    Register.place(x=230, y=225)

    def BackToLogin():
        #Remove os widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        NumberLabel.place(x=5000)
        NumberEntry.place(x=5000)
        Back.place(x=5000)
        NumberLabel.place(x=5000)
        #Trazendo os widgets de volta
        LoginButton.place(x=150, y=225)
        RegisterButton.place(x=230, y=225)

        RecoverPassword = ttk.Button(RightFrame, text='Recover Pass', width =20, command=Recover)
        RecoverPassword.place(x=160, y=255)
        

    
    Back = ttk.Button(RightFrame, text="Back", width=10, command=BackToLogin)
    Back.place(x=150, y=225)




        
jan = Tk()
jan.title('Acess Panel')
jan.geometry('600x300')
jan.configure(background="White")
jan.resizable(width=FALSE, height=FALSE) #Não consegue aumentar nem diminuir a tela

def janela2():
    jan.destroy()
    jan2 = Tk()
    jan2.title('janela2')
    jan2.geometry('600x300')
    jan2.configure(background="#363636")
    jan2.resizable(width=FALSE, height=FALSE) #Não consegue aumentar nem diminuir a tela
    l_nome = Label(jan2, text='Usuario confirmado, \n siga os próximos passos para \n recuperar a senha', anchor=NE, bg='#363636', font='Ivy 25', fg='white')
    l_nome.place(x=0, y=0)



#Carregando Imagens -----------------------



#---------------Widgets--------------------
LeftFrame = Frame(jan, width=200, height=300, bg="#363636", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=390, height=300, bg="#363636", relief="raise")
RightFrame.pack(side=RIGHT)


UserLabel = Label(RightFrame, text='Username:', font=('Century Gothic', 20), bg='#363636', fg='white')
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=113)

PassLabel = Label(RightFrame, text='Password:', font=('Century Gothic', 20), bg='#363636', fg='white')
PassLabel.place(x=5, y=140)

PassEntry = ttk.Entry(RightFrame, width=30, show='*')
PassEntry.place(x=150, y=150)



LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=Login)
LoginButton.place(x=150, y=225)

RegisterButton = ttk.Button(RightFrame, text="Register", width=10, command=Register)
RegisterButton.place(x=230, y=225)

RecoverPassword = ttk.Button(RightFrame, text='Recover Pass', width =20, command=Recover)
RecoverPassword.place(x=160, y=255)

jan.mainloop()