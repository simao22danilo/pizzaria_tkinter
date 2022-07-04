from tkinter import *
import time
import random
from tkinter import messagebox

class Pizza:
    #Tela Principal---------------------------------------------
    def main(sf):
        try:
            sf.scr.destroy()
            sf.scr=Tk()
        except:
            try:
                sf.scr=Tk()
            except:
                pass

        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.mainf1 = Frame(sf.scr, height=150,width=1350)
        sf.logo = PhotoImage(file = 'logo1.png')
        sf.l = Label(sf.mainf1, image = sf.logo)
        sf.l.place(x=0,y=0)
        sf.mainf1.pack(fill=BOTH, expand=1)

        sf.mainf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.mainf2, height=550, width=1350)
        sf.c.pack()
        sf.back = PhotoImage(file='pizzamain.png')
        sf.c.create_image(683,284,image=sf.back)
       
        sf.lab = Button(sf.mainf2, text='MENU',command=lambda:sf.Login(),cursor='hand2',bd=2,font=('cooper black',10,'bold'),fg='white',bg='green')
        sf.lab.place(x=250,y=15)     
        sf.mainf2.pack(fill=BOTH, expand=1)

        sf.scr.mainloop()

     #Tela Login---------------------------------------------
    def Login(sf):
        sf.scr.destroy()
        sf.scr = Tk()

        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.loginf1 = Frame(sf.scr, height=150,width=1350)
        sf.logo = PhotoImage(file = 'logo.png')
        sf.ba = Label(sf.loginf1, image = sf.logo,height=150).place(x=0,y=0)
        

        sf.home = Button(sf.loginf1, text='Home', command=lambda:sf.main(),cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.home.place(x=800,y=100)     
        
        sf.adlog = Button(sf.loginf1, text='Administrador Login',command=lambda:sf.Adminlogin(), cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.adlog.place(x=925,y=100)

        sf.abt = Button(sf.loginf1, text='Sobre nós', cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.abt.place(x=1210,y=100)
        sf.abt.config(command=lambda:sf.about())
        sf.loginf1.pack(fill=BOTH, expand=1)

        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.tim = Label(sf.loginf1,text=sf.localtime,fg='white',font=('default',16),bg='#0b1335')
        sf.tim.place(x=925,y=50)
        sf.loginf1.pack(fill=BOTH, expand=1)

        sf.loginf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.loginf2, height=550, width=1350)
        sf.c.pack()
        

        sf.logo1 = PhotoImage(file='pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)

        sf.c.create_rectangle(50,100,700,450,fill='#d3ede6',outline='white',width=6)
        sf.log = Label(sf.loginf2, text='Curso de Python : Login',fg='white',font=('cooper black',26),bg='#0b1335', width=26)
        sf.log.place(x=59,y=105)

        sf.lab1 = Label(sf.loginf2, text='Usuario :',fg='white',font=('cooper black',22),bg='#0b1335', width=10)
        sf.lab1.place(x=100,y=180)

        sf.user = Entry(sf.loginf2, fg='black',font=('cooper black',22),bg='white', width=20, bd=1, justify='left')
        sf.user.place(x=320,y=180)

        sf.lab2 = Label(sf.loginf2, text='Senha :',fg='white',font=('cooper black',22),bg='#0b1335', width=10)
        sf.lab2.place(x=105,y=250)

        sf.pasd = Entry(sf.loginf2, fg='black',font=('cooper black',22),bg='white', width=20, bd=1, justify='left')
        sf.pasd.place(x=320,y=250)

        sf.lg = Button(sf.loginf2, text='Login',command=lambda:sf.logindatabase(),fg='white',bg='green',cursor='hand2', font=('cooper black',20,'bold'),bd=1)
        sf.lg.place(x=200,y=320)

        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)

        sf.lg = Button(sf.loginf2, text='Limpar',command=lambda:clear(sf), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.lg.place(x=450,y=320)

        sf.rg = Button(sf.loginf2, text='Formulario Registrar', command=lambda:sf.Register(), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.rg.place(x=200,y=390)

        sf.loginf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

     #Tela Sobre---------------------------------------------
    def about(sf):
        sf.src1=Tk()
        sf.src1.geometry('400x550')
        sf.src1.config(bg='light pink')
        sf.src1.title('Sobre nós :')
        sf.src1.iconbitmap('p.ico')
        sf.L = Label(sf.src1, text='\n Pizzaria Sangiorgio\nSeja Bem Vindo\n\n Telefone de contato: \n 65-99999-9999\n\n Ligue para obter \nmais informações\n\nHorário de funcionamento: \n\n todos os dias\n a partir das 18:00',font=('cooper black',20),bg='light pink')
        sf.L.pack()
        sf.src1.mainloop()

     #Tela Administrador---------------------------------------------

    def Adminlogin(sf):
        sf.scr.destroy()
        sf.scr = Tk()

        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.adminf1 = Frame(sf.scr, height=150,width=1350)

        
        sf.c = Canvas(sf.adminf1, height=150, width=1350)
        sf.c.pack()        
        sf.logo = PhotoImage(file = 'logo.png')

        sf.c.create_image (683,75, image=sf.logo)
        sf.home = Button(sf.adminf1, text='Home', command=lambda:sf.main(),cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.home.place(x=1000,y=90)            
       

        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.tim = Label(sf.adminf1,text=sf.localtime,fg='white',font=('default',16),bg='#0b1335')
        sf.tim.place(x=1000,y=50)
        sf.adminf1.pack(fill=BOTH, expand=1)  

        sf.adminf2 = Frame(sf.scr, height=618,width=1350)
        
        sf.c = Canvas(sf.adminf2, height=618, width=1350)
        sf.c.pack()        
        
        sf.logo1 = PhotoImage(file='pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)

        sf.c.create_rectangle(350,100,1016,450,fill='#d3ede6',outline='white',width=6)
        sf.log = Label(sf.adminf2, text='Formulario Login Administrador',fg='white',font=('cooper black',24),bg='#0b1335', width=30)
        sf.log.place(x=350,y=110)

        sf.lab1 = Label(sf.adminf2, text='Usuario :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab1.place(x=400,y=200)

        sf.usera = Entry(sf.adminf2, fg='black',font=('cooper black',18),bg='white', width=15, bd=1, justify='left')
        sf.usera.place(x=650,y=200)

        sf.lab2 = Label(sf.adminf2, text='Senha :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab2.place(x=405,y=270)

        sf.pasda = Entry(sf.adminf2, fg='black',font=('cooper black',18),bg='white', width=20, bd=1, justify='left')
        sf.pasda.place(x=650,y=270)

        
        sf.lg = Button(sf.adminf2, text='Login',command=lambda:sf.admindatabase(), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.lg.place(x=650,y=350)

        sf.bc = Button(sf.adminf2, text='Voltar',command=lambda:sf.Login(), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.bc.place(x=400,y=350)

        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)

        sf.cl = Button(sf.adminf2, text='Limpar',command=lambda:clear(sf), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.cl.place(x=850,y=350)

        sf.adminf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()   

        #Tela Registrar---------------------------------------------

    def Register(sf):
        sf.scr.destroy()
        sf.scr = Tk()

        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.regf1 = Frame(sf.scr, height=150,width=1350)
        sf.logo = PhotoImage(file = 'logo.png')
        sf.ba = Label(sf.regf1, image = sf.logo,height=150).place(x=0,y=0)
        

        sf.home = Button(sf.regf1, text='Home', command=lambda:sf.main(),cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.home.place(x=800,y=100)     
        
        sf.adlog = Button(sf.regf1, text='Administrador Login',command=lambda:sf.Adminlogin(sf), cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.adlog.place(x=950,y=100)

        sf.abt = Button(sf.regf1, text='Sobre nós', cursor='hand2',bd=2,font=('cooper black',16,'bold'),fg='white',bg='green')
        sf.abt.place(x=1210,y=100)
        sf.abt.config(command=lambda:sf.about())
        sf.regf1.pack(fill=BOTH, expand=1)

        sf.localtime = time.asctime(time.localtime(time.time()))
        sf.tim = Label(sf.regf1,text=sf.localtime,fg='white',font=('default',16),bg='#0b1335')
        sf.tim.place(x=925,y=50)
        sf.regf1.pack(fill=BOTH, expand=1)

        sf.regf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.regf2, height=550, width=1350)
        sf.c.pack()
        

        sf.logo1 = PhotoImage(file='pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)

        sf.c.create_rectangle(150,100,1216,450,fill='#d3ede6',outline='white',width=6)
        sf.log = Label(sf.regf2, text='Formulario Cadastrar Usuario ou Admin',fg='white',font=('cooper black',24),bg='#0b1335', width=30)
        sf.log.place(x=350,y=110)

        sf.lab1 = Label(sf.regf2, text='Nome :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab1.place(x=190,y=200)

        sf.first = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=15, bd=1, justify='left')
        sf.first.place(x=430,y=200)

        sf.lab2 = Label(sf.regf2, text='Sobrenome :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab2.place(x=730,y=200)

        sf.last = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=20, bd=1, justify='left')
        sf.last.place(x=920,y=200)

        sf.lab3 = Label(sf.regf2, text='Usuário :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab3.place(x=190,y=250)

        sf.usern = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=20, bd=1, justify='left')
        sf.usern.place(x=430,y=250)

        sf.lab4 = Label(sf.regf2, text='Senha :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab4.place(x=730,y=250)

        sf.passd = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=15, bd=1, justify='left')
        sf.passd.place(x=920,y=250)

        sf.lab5 = Label(sf.regf2, text='E-mail :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab5.place(x=190,y=300)

        sf.email = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=15, bd=1, justify='left')
        sf.email.place(x=430,y=300)

        sf.lab6 = Label(sf.regf2, text='Telefone :',fg='white',font=('cooper black',18),bg='#0b1335', width=10)
        sf.lab6.place(x=730,y=300)

        sf.mob = Entry(sf.regf2, fg='black',font=('cooper black',18),bg='white', width=15, bd=1, justify='left')
        sf.mob.place(x=920,y=300)

        sf.bc = Button(sf.regf2, text='Voltar',command=lambda:sf.Login(), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.bc.place(x=370,y=370)

        sf.rg = Button(sf.regf2, text='Registrar', cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)            

        sf.cl = Button(sf.regf2, text='Limpar',command=lambda:clear(sf), cursor='hand2',font=('cooper black',20,'bold'),fg='white',bg='green',bd=1)
        sf.cl.place(x=910,y=370)

        sf.regf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()    

     #Tela Adminmain---------------------------------------------
    def adminmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x768')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.adminf1 = Frame(sf.scr,bg="#f2e8b8", height=150, width=1350)
        sf.adminf1.pack(side=TOP, fill=BOTH)
        sf.c = Canvas(sf.adminf1, height=150,bg="#f2e8b8", width=1350)
        sf.c.pack()

        sf.logo = PhotoImage(file='logo2.png')
        sf.c.create_image(683,50,image=sf.logo)

        sf.localtime = time.asctime(time.localtime(time.time()))

        sf.c.create_text(900,50,text=sf.localtime,fill='white',font=('default',16))    
        sf.c.create_text(683,125, text='Area Administrativa',font=('cooper black',25,'bold', 'underline'))
       
        sf.out = Button(sf.adminf1, text='Sair',command=lambda:sf.Adminlogin(), cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        
        sf.out.place(x=1100,y=25)

        def reset(sf):
            sf.admainf2 = Frame(sf.scr, width=130, bg='#f2e8b8', height=618, relief=SUNKEN)
            sf.admainf2.pack(side=BOTTOM, fill=BOTH, expand=1)

        sf.vp1=StringVar()
        sf.vp2=StringVar()
        sf.vp3=StringVar()
        sf.vp4=StringVar()

        reset(sf)
        sf.l=["Media","Grande", "Pequena"]

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=0, column=1)
        sf.lbl1=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Pizza Vegetal', bd=10,anchor='w')
        sf.lbl1.place(x=180,y=0)
        sf.lbl11=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=6, bg = '#f2e8b8',text='Itens', bd=6,anchor='w')
        sf.lbl11.grid(row=1, column=0)
        sf.lbl12=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=7, bg = '#f2e8b8',text='Tamanho', bd=6,anchor='w')
        sf.lbl12.grid(row=1, column=1)
        sf.lbl13=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=10, bg = '#f2e8b8',text='Quantidade', bd=6,anchor='w')
        sf.lbl13.grid(row=1, column=2, padx=4)

        sf.lbldel=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Pizza Delux',fg='#7769ad', bd=6, anchor='w')
        sf.lbldel.grid(row=2, column=0)
        sf.opdel =OptionMenu(sf.admainf2,sf.vp1,*sf.l)
        sf.opdel.config(width=6, bd=1)
        sf.opdel.grid(row=2, column=1)
        sf.txtdel = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtdel.grid(row=2, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Pizza Vegetariana',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=3, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp2,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=3, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=3, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Pizza Calabresa',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=4, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp3,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=4, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=4, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Pizza Peperone',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=5, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp4,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=5, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=5, column=2)

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=0, column=5)

        sf.lbl3=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Especial do dia', bd=10,anchor='w')
        sf.lbl3.place(x=550,y=0)

        sf.lbl31=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=6, bg = '#f2e8b8',text='Itens', bd=6,anchor='w')
        sf.lbl31.grid(row=1, column=4)

        sf.lbl33=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=10, bg = '#f2e8b8',text='Quantidade', bd=6,anchor='w')
        sf.lbl33.grid(row=1, column=5)

        sf.lblros=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Frango',fg='#7769ad', bd=6,anchor='w')
        sf.lblros.grid(row=2, column=4)
        
        sf.txtros=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,width=4, bg = 'powder blue',justify='right')
        sf.txtros.grid(row=2, column=5)

        sf.lblmeat=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Almondegas',fg='#7769ad', bd=6,anchor='w')
        sf.lblmeat.grid(row=3, column=4)

        sf.txtmeat=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,width=4, bg = 'powder blue',justify='right')
        sf.txtmeat.grid(row=3, column=5)

        sf.lblbon=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Peito Frango',fg='#7769ad', bd=6,anchor='w')
        sf.lblbon.grid(row=4, column=4)
        
        sf.txtbon=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=4, justify='right')
        sf.txtbon.grid(row=4, column=5)

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=0, column=8)

        sf.lbl6=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Detalhes Cliente', bd=10,anchor='w')
        sf.lbl6.place(x=970,y=0)

        sf.lblbnam=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Nome',fg='#7769ad', bd=6,anchor='w')
        sf.lblbnam.grid(row=1, column=7)
        
        sf.txtnam=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txtnam.grid(row=1, column=8)

        sf.lblmob=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Telefone ',fg='#7769ad', bd=6,anchor='w')
        sf.lblmob.grid(row=2, column=7)
        
        sf.txtmob=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txtmob.grid(row=2, column=8)       

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=3, column=8)

        sf.lbl5=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Pagamento', bd=10,anchor='w')
        sf.lbl5.place(x=1000,y=140)
        
        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=4, column=6)
        sf.lblord=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Nota ',fg='#7769ad', bd=6,anchor='w')
        sf.lblord.grid(row=4, column=7)        
        sf.txtord=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txtord.grid(row=4, column=8) 

        sf.lblco=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Subtotal ',fg='#7769ad', bd=6,anchor='w')
        sf.lblco.grid(row=5, column=7)        
        sf.txtco=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txtco.grid(row=5, column=8) 

        sf.lblser=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Serviços ',fg='#7769ad', bd=6,anchor='w')
        sf.lblser.grid(row=6, column=7)        
        sf.txtser=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txtser.grid(row=6, column=8)

        sf.lbltax=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Imposto ',fg='#7769ad', bd=6,anchor='w')
        sf.lbltax.grid(row=7, column=7)        
        sf.txttax=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txttax.grid(row=7, column=8) 

        sf.lbltot=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Total ',fg='#7769ad', bd=6,anchor='w')
        sf.lbltot.grid(row=8, column=7)        
        sf.txttot=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=30, justify='right')
        sf.txttot.grid(row=8, column=8) 

        sf.btnprice = Button(sf.admainf2,command=lambda:sf.price(), pady=2,bd=1, fg='black', font=('ariel', 16, 'bold'), width=6, text='Preço',  anchor='w')
        sf.btnprice.place(x=970,y=440)

        sf.btnTotal = Button(sf.admainf2, pady=2,bd=1, fg='black', font=('ariel', 16, 'bold'), width=6, text='Total',  anchor='w')
        sf.btnTotal.place(x=1160,y=440)

        sf.btnreset = Button(sf.admainf2, pady=2,bd=1, fg='black', font=('ariel', 16, 'bold'), width=6, text='Limpar',  anchor='w')
        sf.btnreset.place(x=970,y=500)

        sf.btnpay = Button(sf.admainf2,command=lambda:sf.adminorderdetaill(), pady=2,bd=1, fg='black', font=('ariel', 16, 'bold'), width=6, text='Pagar',  anchor='w')
        sf.btnpay.place(x=1160,y=500)

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=6, column=1)
        sf.lbl10=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Não Vegetariana', bd=10,anchor='w')
        sf.lbl10.place(x=180,y=270)
        sf.lbl110=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=6, bg = '#f2e8b8',text='Itens', bd=6,anchor='w')
        sf.lbl110.grid(row=7, column=0)
        sf.lbl120=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=7, bg = '#f2e8b8',text='Tamanho', bd=6,anchor='w')
        sf.lbl120.grid(row=7, column=1)
        sf.lbl130=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=10, bg = '#f2e8b8',text='Quantidade', bd=6,anchor='w')
        sf.lbl130.grid(row=7, column=2, padx=4)

        sf.lbldel0=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Não Vegana',fg='#7769ad', bd=6, anchor='w')
        sf.lbldel0.grid(row=8, column=0)
        sf.opdel0 =OptionMenu(sf.admainf2,sf.vp1,*sf.l)
        sf.opdel0.config(width=6, bd=1)
        sf.opdel0.grid(row=8, column=1)
        sf.txtdel0 = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtdel0.grid(row=8, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Peito Frango',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=9, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp2,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=9, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=9, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Salsicha Frango',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=10, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp3,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=10, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=10, column=2)

        sf.lblvaga=Label(sf.admainf2, pady=2, font=('ariel',16, 'bold'), bg='#f2e8b8',text='Frango',fg='#7769ad', bd=6, anchor='w')
        sf.lblvaga.grid(row=11, column=0)
        sf.opvaga =OptionMenu(sf.admainf2,sf.vp4,*sf.l)
        sf.opvaga.config(width=6, bd=1)
        sf.opvaga.grid(row=11, column=1)
        sf.txtvaga = Entry(sf.admainf2, font=("ariel",16,'bold'),bd=1,bg="powder blue", width=4,justify='right')
        sf.txtvaga.grid(row=11, column=2)

        sf.nom= Label(sf.admainf2, pady=2, text=(''), font=('cooper black', 20), bg = '#f2e8b8', bd=10, anchor='w')
        sf.nom.grid(row=6, column=5)

        sf.lbl3=Label(sf.admainf2, pady=2, font=('cooper black', 20, 'bold','underline'), bg = '#f2e8b8',text='Aperitivos e Bebidas', bd=10,anchor='w')
        sf.lbl3.place(x=450,y=270)

        sf.lbl31=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=6, bg = '#f2e8b8',text='Itens', bd=6,anchor='w')
        sf.lbl31.grid(row=7, column=4)

        sf.lbl33=Label(sf.admainf2, pady=2, font=('cooper black', 16,'underline'),width=10, bg = '#f2e8b8',text='Quantidade', bd=6,anchor='w')
        sf.lbl33.grid(row=7, column=5)

        sf.lblros=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Coca Cola',fg='#7769ad', bd=6,anchor='w')
        sf.lblros.grid(row=8, column=4)
        
        sf.txtros=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,width=4, bg = 'powder blue',justify='right')
        sf.txtros.grid(row=8, column=5)

        sf.lblmeat=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Burger Pizza',fg='#7769ad', bd=6,anchor='w')
        sf.lblmeat.grid(row=9, column=4)

        sf.txtmeat=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,width=4, bg = 'powder blue',justify='right')
        sf.txtmeat.grid(row=9, column=5)

        sf.lblbon=Label(sf.admainf2, pady=2, font=('aria', 16,'bold'),width=10, bg = '#f2e8b8',text='Batata',fg='#7769ad', bd=6,anchor='w')
        sf.lblbon.grid(row=10, column=4)
        
        sf.txtbon=Entry(sf.admainf2,  font=('ariel', 16,'bold'),bd=1,bg = 'powder blue',width=4, justify='right')
        sf.txtbon.grid(row=10, column=5)

    #Tela menulist---------------------------------------------

    def menulist(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.menuf1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.menuf1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.menuf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)
        sf.c.create_text(950,80,text='Seja Bem Vindo', fill='white',font=('default',20))        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.menuf1.pack(fill=BOTH, expand=1)

        sf.menuf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.menuf2, height=550, width=1350)
        sf.c.pack()       
        sf.logo1 = PhotoImage(file = 'pizzamain.png')     
        sf.c.create_image(683,309,image=sf.logo1)        
        sf.c.create_rectangle(50,140,1316,420, fill='#d3ede6',outline='white',width=6)
        sf.veg=PhotoImage(file = 'veg.png')
        sf.c.create_image(230,250,image=sf.veg)        
        sf.vegbut= Button(sf.menuf2,text='Pizza Vegetal',command=lambda:sf.vegpizza(sf.x),cursor='hand2',fg='white',bg='green',font=('default',20),bd=5)
        sf.vegbut.place(x=170,y=350)
        sf.nonveg=PhotoImage(file = 'non.png')
        sf.c.create_image(530,250,image=sf.nonveg)
        sf.nonvegbut= Button(sf.menuf2,text='Pizza Especial',command=lambda:sf.nonvegpizza(sf.x),cursor='hand2',fg='white',bg='green',font=('default',20),bd=5)
        sf.nonvegbut.place(x=440,y=350) 
        sf.chi=PhotoImage(file = 'chiken.png')
        sf.c.create_image(830,250,image=sf.chi)
        sf.chibut= Button(sf.menuf2,text='Frango Especial',command=lambda:sf.SpecialChi(sf.x),cursor='hand2',fg='white',bg='green',font=('default',20),bd=5)
        sf.chibut.place(x=730,y=350) 
        sf.side=PhotoImage(file = 'extra.png')
        sf.c.create_image(1130,250,image=sf.side)
        sf.sidebut= Button(sf.menuf2,text='Aperitivos | Bebidas',command=lambda:sf.sidebev(sf.x),cursor='hand2',fg='white',bg='green',font=('default',20),bd=5)
        sf.sidebut.place(x=1000,y=350)        
        sf.menuf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    #Tela pizmain---------------------------------------------

    def pizmain(sf):
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.pizf1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.pizf1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.c.create_text(950,80,text='Seja Bem Vindo', fill='white',font=('default',20))
        sf.name='Curso - Tkinter'
        sf.c.create_text(950,120,text=sf.name, fill='white',font=('default',18))  
        sf.out=Button(sf.pizf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
          
        sf.out.place(x=1200,y=100)
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,40,text=sf.localtime, fill='white',font=('default',16))
        sf.pizf1.pack(fill=BOTH, expand=1)

        sf.pizf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.pizf2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(400,120,966,470, fill='#d3ede6',outline='white',width=2)
        sf.deli=PhotoImage(file = 'delivery.png')
        sf.c.create_image(540,260,image=sf.deli)
        sf.pic=PhotoImage(file = 'pick.png')
        sf.c.create_image(825,260,image=sf.pic)
        sf.de= Button(sf.pizf2,text='Entregar',command=lambda:sf.menulist('deli'),cursor='hand2',fg='white',bg='#0b1335',font=('default',20),bd=5)
        sf.de.place(x=480,y=400)
        sf.de= Button(sf.pizf2,text='Pegar',cursor='hand2',fg='white',bg='#0b1335',font=('default',20),bd=5)
        sf.de.place(x=770,y=400)
        sf.c.create_rectangle(405,125,678,465, outline='black',width=2)
        sf.c.create_rectangle(688,125,960,465, outline='black',width=2)
        sf.pizf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

      #Tela vegpizza---------------------------------------------

    def vegpizza(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.vegf1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.vegf1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.vegf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,80,text=sf.localtime, fill='white',font=('default',16))
        sf.vegf1.pack(fill=BOTH, expand=1)

        sf.vegf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.vegf2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.vegf2, text='Pizza Vegetais',bg='#d3ede6',font=('cooper black',22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(400,40,966,540,fill='#d3ede6',outline='white',width=6)

        sf.c.create_rectangle(405,50,960,170,width=2)
        sf.delu=PhotoImage(file = 'deluxe.png')
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Vegetal Deluxe",fill='#000000',font=('cooper black',20))
        sf.c.create_text(860,80,text="R$30 / R$40 / R$50" ,fill='#ff3838',font=('default',16,'bold'))

        sf.cl1=Radiobutton(sf.vegf2,text='Pequena',bg='blue',value=10)
        sf.cl1.place(x=550,y=100)
        sf.cl2=Radiobutton(sf.vegf2,text='Média',bg='blue',value=20)
        sf.cl2.place(x=650,y=100)
        sf.cl3=Radiobutton(sf.vegf2,text='Grande',bg='blue',value=30)
        sf.cl3.place(x=750,y=100)

        sf.c.create_text(590,150,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty1=Entry(sf.vegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty1.place(x=650,y=140)
        sf.add1=Button(sf.vegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add1.place(x=750,y=130)

        sf.c.create_rectangle(405,170,960,290,width=2)
        sf.vag=PhotoImage(file = 'extravaganza.png')
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Pizza Vaganza",fill='#000000',font=('cooper black',20))
        sf.c.create_text(860,200,text="R$25 / R$35 / R$45" ,fill='#ff3838',font=('default',16,'bold'))

        sf.cl21=Radiobutton(sf.vegf2,text='Pequena',bg='blue',value=10)
        sf.cl21.place(x=550,y=220)
        sf.cl22=Radiobutton(sf.vegf2,text='Média',bg='blue',value=20)
        sf.cl22.place(x=650,y=220)
        sf.cl23=Radiobutton(sf.vegf2,text='Grande',bg='blue',value=30)
        sf.cl23.place(x=750,y=220)

        sf.c.create_text(590,270,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty2=Entry(sf.vegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty2.place(x=650,y=260)
        sf.add2=Button(sf.vegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add2.place(x=750,y=250)

        sf.c.create_rectangle(405,290,960,410,width=2)
        sf.pep=PhotoImage(file = '5-pepper-veg-pizza.png')
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Pimentão",fill='#000000',font=('cooper black',20))
        sf.c.create_text(860,320,text="R$35 / R$45 / R$55" ,fill='#ff3838',font=('default',16,'bold'))

        sf.cl31=Radiobutton(sf.vegf2,text='Pequena',bg='blue',value=10)
        sf.cl31.place(x=550,y=340)
        sf.cl32=Radiobutton(sf.vegf2,text='Média',bg='blue',value=20)
        sf.cl32.place(x=650,y=340)
        sf.cl33=Radiobutton(sf.vegf2,text='Grande',bg='blue',value=30)
        sf.cl33.place(x=750,y=340)

        sf.c.create_text(590,390,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty3=Entry(sf.vegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty3.place(x=650,y=380)
        sf.add3=Button(sf.vegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add3.place(x=750,y=370)

        sf.c.create_rectangle(405,410,960,530,width=2)
        sf.mag=PhotoImage(file = 'Margherit.png')
        sf.c.create_image(470,470,image=sf.mag)
        sf.c.create_text(650,440,text="Margherita",fill='#000000',font=('cooper black',20))
        sf.c.create_text(860,440,text="R$30 / R$40 / R$50" ,fill='#ff3838',font=('default',16,'bold'))

        sf.cl41=Radiobutton(sf.vegf2,text='Pequena',bg='blue',value=10)
        sf.cl41.place(x=550,y=460)
        sf.cl42=Radiobutton(sf.vegf2,text='Média',bg='blue',value=20)
        sf.cl42.place(x=650,y=460)
        sf.cl43=Radiobutton(sf.vegf2,text='Grande',bg='blue',value=30)
        sf.cl43.place(x=750,y=460)

        sf.c.create_text(590,510,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty4=Entry(sf.vegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty4.place(x=650,y=500)
        sf.add4=Button(sf.vegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add4.place(x=750,y=490)

        sf.con=Button(sf.vegf2,text='Confirmar Pedido',command=lambda:sf.Orderde(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.con.place(x=1000,y=60)
        sf.more=Button(sf.vegf2,text='Adicionar +',command=lambda:sf.menulist('deli'),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.more.place(x=1000,y=110)



        sf.vegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    def nonvegpizza(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.nonvegf1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.nonvegf1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.nonvegf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.nonvegf1.pack(fill=BOTH, expand=1)

        sf.nonvegf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.nonvegf2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.nonvegf2, text='Pizzas Especiais',bg='#d3ede6',font=('cooper black',22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(400,40,966,540,fill='#d3ede6',outline='white',width=6)

        sf.c.create_rectangle(405,50,960,170,width=2)
        sf.delu=PhotoImage(file = 'Non-Veg_Supreme.png')
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Suprema não Vegana",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,80,text="R$30 / R$40 / R$50" ,fill='#ff3838',font=('default',16,'bold'))

        
        sf.cs1=Radiobutton(sf.nonvegf2,text='Pequena',bg='blue',value=10)
        sf.cs1.place(x=550,y=100)
        sf.cs2=Radiobutton(sf.nonvegf2,text='Média',bg='blue',value=20)
        sf.cs2.place(x=650,y=100)
        sf.cs3=Radiobutton(sf.nonvegf2,text='Grande',bg='blue',value=30)
        sf.cs3.place(x=750,y=100)
        
        sf.c.create_text(590,150,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty5=Entry(sf.nonvegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty5.place(x=650,y=140)
        sf.add5=Button(sf.nonvegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add5.place(x=750,y=130)

        sf.c.create_rectangle(405,170,960,290,width=2)
        sf.vag=PhotoImage(file = 'nonChicken_Tikka.png')
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Frango Tikka",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,200,text="R$25 / R$35 / R$45" ,fill='#ff3838',font=('default',16,'bold'))
                
        sf.c61=Radiobutton(sf.nonvegf2,text='Pequena',bg='blue',value=10)
        sf.c61.place(x=550,y=220)
        sf.c62=Radiobutton(sf.nonvegf2,text='Média',bg='blue',value=20)
        sf.c62.place(x=650,y=220)
        sf.c63=Radiobutton(sf.nonvegf2,text='Grande',bg='blue',value=30)
        sf.c63.place(x=750,y=220)
        
        sf.c.create_text(590,270,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty6=Entry(sf.nonvegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty6.place(x=650,y=260)
        sf.add6=Button(sf.nonvegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add6.place(x=750,y=250)

        sf.c.create_rectangle(405,290,960,410,width=2)
        sf.pep=PhotoImage(file = 'no-LoadedL.png')
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Chiken Pearl",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,320,text="R$35 / R$45 / R$55" ,fill='#ff3838',font=('default',16,'bold'))
        
        sf.c81=Radiobutton(sf.nonvegf2,text='Pequena',bg='blue',value=10)
        sf.c81.place(x=550,y=340)
        sf.c82=Radiobutton(sf.nonvegf2,text='Média',bg='blue',value=20)
        sf.c82.place(x=650,y=340)
        sf.c83=Radiobutton(sf.nonvegf2,text='Grande',bg='blue',value=30)
        sf.c83.place(x=750,y=340)
        
        sf.c.create_text(590,390,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty8=Entry(sf.nonvegf2,bg='powder blue',font=('default',12),width=4)
        sf.qty8.place(x=650,y=380)
        sf.add8=Button(sf.nonvegf2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add8.place(x=750,y=370)       


        sf.con=Button(sf.nonvegf2,text='Confirmar Pedido',command=lambda:sf.Orderde(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.con.place(x=1000,y=60)
        sf.more=Button(sf.nonvegf2,text='Adicionar +',command=lambda:sf.menulist(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.more.place(x=1000,y=110)



        sf.nonvegf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    def SpecialChi(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.spef1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.spef1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.spef1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.spef1.pack(fill=BOTH, expand=1)

        sf.spef2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.spef2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.spef2, text='Frango Especiais',bg='#d3ede6',font=('cooper black',22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(400,40,966,420,fill='#d3ede6',outline='white',width=6)

        sf.c.create_rectangle(405,50,960,170,width=2, outline='blue')
        sf.delu=PhotoImage(file = 'roasted.png')
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Frango Assado",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,80,text="R$50" ,fill='#ff3838',font=('default',16,'bold'))
       
        sf.c.create_text(590,150,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty9=Entry(sf.spef2,bg='powder blue',font=('default',12),width=4)
        sf.qty9.place(x=650,y=140)
        sf.add9=Button(sf.spef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add9.place(x=750,y=130)

        sf.c.create_rectangle(405,170,960,290,width=2)
        sf.vag=PhotoImage(file = 'chicken-meatballs.jpg')
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Almôndegas de Frango",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,200,text=" R$35" ,fill='#ff3838',font=('default',16,'bold'))
                 
        sf.c.create_text(590,270,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty10=Entry(sf.spef2,bg='powder blue',font=('default',12),width=4)
        sf.qty10.place(x=650,y=260)
        sf.add10=Button(sf.spef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add10.place(x=750,y=250)

        sf.c.create_rectangle(405,290,960,410,width=2)
        sf.pep=PhotoImage(file = 'Boneless-Chicken-wings-192x192.png')
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Frango Desossado",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,320,text="R$45" ,fill='#ff3838',font=('default',16,'bold'))
        
               
        sf.c.create_text(590,390,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty11=Entry(sf.spef2,bg='powder blue',font=('default',12),width=4)
        sf.qty11.place(x=650,y=380)
        sf.add11=Button(sf.spef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add11.place(x=750,y=370)       


        sf.con=Button(sf.spef2,text='Confirmar Pedido',command=lambda:sf.Orderde(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.con.place(x=1000,y=60)
        sf.more=Button(sf.spef2,text='Adicionar +',command=lambda:sf.menulist(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.more.place(x=1000,y=110)



        sf.spef2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()

    def sidebev(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        sf.sidef1 = Frame(sf.scr, height=150,width=1350)
        sf.c= Canvas(sf.sidef1,height=150,width=1350)
        sf.c.pack()
        sf.logo = PhotoImage(file = 'logo.png')     
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.sidef1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.sidef1.pack(fill=BOTH, expand=1)

        sf.sidef2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.sidef2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.sidef2, text='Aperitivos | Bebidas',bg='#d3ede6',font=('cooper black',22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(400,40,966,420,fill='#d3ede6',outline='white',width=6)

        sf.c.create_rectangle(405,50,960,170,width=2, outline='blue')
        sf.delu=PhotoImage(file = 'coke.png')
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Coca - Cola",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,80,text="R$10" ,fill='#ff3838',font=('default',16,'bold'))
       
        sf.c.create_text(590,150,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty12=Entry(sf.sidef2,bg='powder blue',font=('default',12),width=4)
        sf.qty12.place(x=650,y=140)
        sf.add12=Button(sf.sidef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add12.place(x=750,y=130)

        sf.c.create_rectangle(405,170,960,290,width=2)
        sf.vag=PhotoImage(file = 'burger.png')
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Hamburguer",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,200,text=" R$15" ,fill='#ff3838',font=('default',16,'bold'))
                 
        sf.c.create_text(590,270,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty13=Entry(sf.sidef2,bg='powder blue',font=('default',12),width=4)
        sf.qty13.place(x=650,y=260)
        sf.add13=Button(sf.sidef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add13.place(x=750,y=250)

        sf.c.create_rectangle(405,290,960,410,width=2)
        sf.pep=PhotoImage(file = 'white.png')
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Macarrão",fill='#000000',font=('cooper black',16))
        sf.c.create_text(860,320,text="R$15" ,fill='#ff3838',font=('default',16,'bold'))
        
               
        sf.c.create_text(590,390,text='Quantidade :',fill='#000000',font=('default',12))
        sf.qty14=Entry(sf.sidef2,bg='powder blue',font=('default',12),width=4)
        sf.qty14.place(x=650,y=380)
        sf.add14=Button(sf.sidef2,text='Adicionar',bg='green',cursor='hand2',fg='white',bd=4, font=('default',12,'bold'))
        sf.add14.place(x=750,y=370)       


        sf.con=Button(sf.sidef2,text='Confirmar Pedido',command=lambda:sf.Orderde(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.con.place(x=1000,y=60)
        sf.more=Button(sf.sidef2,text='Adicionar +',command=lambda:sf.menulist(sf.x),bg='green', cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.more.place(x=1000,y=110)



        sf.sidef2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()



    def logindatabase(sf):
        pass
        sf.pizmain()

    def regdatabase(sf):
        pass

    def admindatabase(sf):
        sf.adminmain()
    
    def Address(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.geometry('1350x700')
        sf.scr.iconbitmap('p.ico')

        
        sf.addf1 = Frame(sf.scr, height=150, width=1350)
        sf.c = Canvas(sf.addf1, height=150, width=1350)
        sf.c.pack()
        sf.logo=PhotoImage(file = 'logo.png')
        sf.c.create_image(683,75,image=sf.logo)
        sf.out=Button(sf.addf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.out.place(x=1200,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.addf1.pack(fill=BOTH, expand=1)

        sf.addf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.addf2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.addf2, text='Endereço:',width=20,bg='#cb133b',fg='white',font=('default',27))
        sf.log.place(x=480,y=110)
        sf.c.create_rectangle(150,100,1216,450,fill='#d3ede6',outline='white',width=6)

        sf.lab1=Label(sf.addf2,text='Cidade :', bg='#d34dec',font=('cooper black',12))
        sf.lab1.place(x=190, y=200)
        sf.city=Entry(sf.addf2,bg='white', width=21,font=('default',10),bd=1)
        sf.city.place(x=430,y=200)
        sf.lab2=Label(sf.addf2,text='Localidade :', bg='#d34dec',font=('cooper black',12))
        sf.lab2.place(x=730, y=200)
        sf.loc=Entry(sf.addf2,bg='white', width=21,font=('default',10),bd=1)
        sf.loc.place(x=918,y=200)        
        sf.lab3=Label(sf.addf2,text='Condomínio :', bg='#d34dec',font=('cooper black',12))
        sf.lab3.place(x=190, y=250)
        sf.buil=Entry(sf.addf2,bg='white', width=21,font=('default',10),bd=1)
        sf.buil.place(x=430,y=250)
        sf.lab4=Label(sf.addf2,text='Casa :', bg='#d34dec',font=('cooper black',12))
        sf.lab4.place(x=730, y=250)
        sf.hom=Entry(sf.addf2,bg='white', width=21,font=('default',10),bd=1)
        sf.hom.place(x=918,y=250)
        sf.lab5=Label(sf.addf2,text='Ponto de Referência :', bg='#d34dec',font=('cooper black',12))
        sf.lab5.place(x=190, y=300)
        sf.lan=Entry(sf.addf2,bg='white', width=21,font=('default',10),bd=1)
        sf.lan.place(x=430,y=300)    

        sf.bc=Button(sf.addf2,text='Voltar',command=lambda:sf.Orderde(sf.x),bg='#d34dec',cursor='hand2',fg='white',bd=1,font=('default',10))
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.addf2,text='Concluir Pedido',bg='#d34dec',cursor='hand2',fg='white',bd=1,font=('default',10,))
        sf.rg.place(x=610,y=370)
        sf.cl=Button(sf.addf2,text='Limpar',bg='#d34dec',cursor='hand2',fg='white',bd=1,font=('default',10,))
        sf.cl.place(x=910,y=370)           

        sf.addf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()  
        
    def Orderde(sf,x):
        sf.x=x
        sf.scr.destroy()
        sf.scr = Tk()
        sf.scr.geometry('1350x700')
        sf.scr.title('Pizzaria Sangiorgio :')
        sf.scr.iconbitmap('p.ico')

        
        sf.ordf1 = Frame(sf.scr, height=150, width=1350)
        sf.c = Canvas(sf.ordf1, height=150, width=1350)
        sf.c.pack()
        sf.logo=PhotoImage(file = 'logo.png')
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.ordf1,text='Sair',command=lambda:sf.Login(),cursor='hand2',font=('cooper black',16,'bold'),fg='white',bg='green',bd=2)
        sf.home.place(x=1000,y=100)        
        sf.localtime = time.asctime(time.localtime(time.time()))        
        sf.c.create_text(1000,50,text=sf.localtime, fill='white',font=('default',16))
        sf.ordf1.pack(fill=BOTH, expand=1)

        sf.ordf2 = Frame(sf.scr, height=550, width=1350)
        sf.c = Canvas(sf.ordf2, height=550, width=1350)
        sf.c.pack()
        sf.logo1=PhotoImage(file = 'pizzamain.png')
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log= Label(sf.ordf2, text='Seu Pedido',bg='green',fg='white',font=('cooper black',22))
        sf.log.place(x=450,y=4)
        sf.c.create_rectangle(250,50,800,500,fill='#d3ede6',outline='white',width=6)

        sf.text='Total : '
        sf.tot=Label(sf.ordf2,text=sf.text, bg='green', fg='white', width=12, font=('cooper black',22))
        sf.tot.place(x=900, y=250)

        if sf.x=="deli":
            sf.y=sf.Address

        sf.pay=Button(sf.ordf2,text='Pagar',command=lambda:sf.y(sf.x),bg='green',cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.pay.place(x=900,y=300)
        sf.exi=Button(sf.ordf2,text='Adicionar +',command=lambda:sf.menulist('deli'),bg='green',cursor='hand2',fg='white',bd=1,font=('default',15,'bold'))
        sf.exi.place(x=1070,y=300)  
        sf.c.create_text(525,80,text='Produto | Tamanho | Quantidade |Preço', font=('cooper black',15))
        sf.c.create_text(525,90,text='___________________________________________', font=('cooper black',15))  

        sf.ordf2.pack(fill=BOTH, expand=1)
        sf.scr.mainloop()  

    def price(sf):
        sf.roo=Tk()
        sf.roo.geometry('950x960')
        sf.roo.title('Lista de Preços')
        sf.roo.iconbitmap('p.ico') 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Produtos',fg='black',bd=5)
        sf.lbinfo.grid(row=0, column=0)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Pizza Vegetais',fg='black',anchor='w')
        sf.lbinfo.grid(row=1, column=1)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='(Pequena/Média/Grande)',fg='black',anchor='w')
        sf.lbinfo.grid(row=1, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Deluxe Vegetal',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=2, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$30/R$40/R$50',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=2, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Vegetal Vaganza',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=3, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$25/R$35/R$45',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=3, column=2)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Pimentão',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=4, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$35/R$45/R$55',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=4, column=2)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Margherita',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=5, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$30/R$40/R$50',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=5, column=2)

        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Pizza Especiais',fg='black',anchor='w')
        sf.lbinfo.grid(row=6, column=1)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='(Pequena/Média/Grande)',fg='black',anchor='w')
        sf.lbinfo.grid(row=6, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Suprema não Vegana',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=7, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$30/R$40/R$50',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=7, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Frango Tikka',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=8, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$25/R$35/R$45',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=8, column=2)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Chiken Pearl',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=9, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$35/R$45/R$55',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=9, column=2)
         

        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Frango Especial',fg='black',anchor='w')
        sf.lbinfo.grid(row=10, column=1)       
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Frango Assado',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=11, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$50',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=11, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Almôndegas de Frango',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=12, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$35',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=12, column=2)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Frango Desossado',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=13, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$45',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=13, column=2)

        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Aperitivos | Bebidas',fg='black',anchor='w')
        sf.lbinfo.grid(row=14, column=1)       
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Coca - Cola',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=15, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$10',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=15, column=2) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Hamburguer',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=16, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$15',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=16, column=2)
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='Macarrão',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=17, column=0) 
        sf.lbinfo = Label(sf.roo, font=('aria',18,'bold'),text='R$15',fg='steel blue',anchor='w')
        sf.lbinfo.grid(row=17, column=2)

        sf.roo.mainloop()

    def adminorderdetaill(sf):
        if messagebox.askyesno('Pagamento:','Deseja realmente finalizar o pagamento?'):
            messagebox.showinfo('Pagamento: ', 'Pagamento completado com sucesso')
            messagebox.showinfo('Pagamento:', 'Vamos trabalhar estes passos nos próximos vídeos ')

        else:
            messagebox.showinfo('Pagamento: ','Vamos trabalhar estes passos nos próximos vídeos')

    
       

        
        
x=Pizza()
x.main()