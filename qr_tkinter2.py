import tkinter
from tkinter import Label, Frame, Entry, Button
import time
import qrcode
from resizeimage import resizeimage






gui = tkinter.Tk()                                # CREO OBJETO TIPO VENTANA
gui.geometry('800x400+400+150')                   # VENTANA POR DEFAULT
gui.minsize(600,350)                              # MINIMO DE VENTANA
icono = tkinter.PhotoImage(file='codigo-qr.png')  # AÑADIR ARCHIVO DE IMAGEN GENERAL
gui.iconphoto(True,icono,icono)                         # CARGAR IMAGEN COMO ICONO A LA VENTANA
gui.resizable(False,False)                       # REDIMENSIONAR VENTANA
gui.title('Qr Generator - Hecho por Jonathan')    # TITULO DE LA VENTANA




#========= HEADER DE LA VENTANA =========
titulo = Label(gui,text='Qr Code Generator', font=('times new roman',40),bg='#02025B',fg='white')
titulo.place(relx=0,rely=0,relwidth=1,)
#========= CONTENEDORES DE WIDGETS =========
frame1 = Frame(gui,border=2)
frame1.config(relief='ridge',bg='white')
frame1.place(relx=0.03, y=80,relwidth=0.56,relheight=0.75)

frame2 = Frame(gui,border=2)
frame2.config(relief='ridge',bg='white')
frame2.place(relx=0.618, y=80,relwidth=0.352,relheight=0.75)    
#========= HEADERS DE CONTENEDORES =========
lframe_1 = Label(frame1, text='Detalles del solicitante',font=('times new roman',14),bg='#02025B',fg='white')
lframe_1.place(relx=0,rely=0,relwidth=1,relheight=0.08)

lframe_2 = Label(frame2,text='Codigo QR',font=('times new roman',14),bg='#02025B',fg='white')
lframe_2.place(relx=0,rely=0,relwidth=1, relheight=0.08)
#========= LABELS CONTENEDOR 1 =========
LF1_relx = 0.1
lname = Label(frame1,text='Nombre',font=('times new roman',14),bg='yellow')
lname.place(relx=LF1_relx, rely=0.15)

linstitucion = Label(frame1,text='Institucion',font=('times new roman',14),bg='yellow')
linstitucion.place(relx=LF1_relx, rely=0.3)

lcargo = Label(frame1,text='Cargo',font=('times new roman',14),bg='yellow')
lcargo.place(relx=LF1_relx, rely=0.45)

lmail = Label(frame1,text='E-mail',font=('times new roman',14),bg='yellow')
lmail.place(relx=LF1_relx, rely=0.6)

lend = Label(frame1,text='Qr Se Generó Correctamente!',font=('times new roman',12),bg='yellow')
lend1 = Label(frame1,text='COMPLETE TODOS LOS DATOS',font=('times new roman',12),bg='yellow')


#========= ENTRY'S CONTENEDOR 1 =========
EF1_relx = 0.4
ename_var = tkinter.StringVar()
einst_var = tkinter.StringVar()
ecarg_var = tkinter.StringVar()
email_var = tkinter.StringVar()

ename = Entry(frame1,bg='lightyellow', textvariable=ename_var)
ename.place(relx=EF1_relx,rely=0.15,relwidth=0.5, relheight=0.1)

einstitucion = Entry(frame1,bg='lightyellow',textvariable=einst_var)
einstitucion.place(relx=EF1_relx,rely=0.3,relwidth=0.5, relheight=0.1)

ecargo = Entry(frame1,bg='lightyellow',textvariable=ecarg_var)
ecargo.place(relx=EF1_relx,rely=0.45,relwidth=0.5, relheight=0.1)

email = Entry(frame1,bg='lightyellow',textvariable=email_var)
email.place(relx=EF1_relx,rely=0.6,relwidth=0.5, relheight=0.1)

#========= LABELS CONTENEDOR 2 =========

lqr_code1 = Label(frame2,text='QR code',font=('times new roman',14),bg='yellow')
lqr_code1.place(relx=0.2, rely=0.15,relwidth=0.6, relheight=0.6)



#========= BUTTOM'S CONTENEDOR 1 =========
def generar():
    global imgn
    if ename_var.get() == "" or einst_var.get() == "" or ecarg_var.get() == "" or email_var.get() == "":
        
        lend1.place(relx=0.25, rely=0.87)
        lend.place(relx=2, rely=2)
        #bgenerar.configure(state='normal')
    else: 
        print(ename_var.get())
        name = ename_var.get().split()
        
        name = ('QR_'+name[0])
        
        # qr_code = qr2.codeqr(ename_var.get(),einst_var.get(),ecarg_var.get(),email_var.get(),name)
        # qr_code.qr_creator()
        
        data = f'FIRMADO POR: {ename_var.get()}\n{ecarg_var.get()}\nRAZON: Firmado electronicamente desde\n{einst_var.get()}\n{email_var.get()}'
        print(data)
        
  
        img = qrcode.make(data)
        img = resizeimage.resize_cover(img,[180,180])
        img.save(f'{name}.png')
        ima = name+'.png'
        
        imgn = tkinter.PhotoImage(file=ima)
        lqr_code1.config(image=imgn)

        lend1.place(relx=2, rely=2)
        lend.place(relx=0.25, rely=0.87)
        
   

def clean():
    ename_var.set('')
    einst_var.set('')
    ecarg_var.set('')
    email_var.set('')
    lqr_code1.config(image='')





           
bgenerar = Button(frame1,text='Generar QR',command=generar,bg='#A006BF',fg='white')
bgenerar.place(relx=0.15, rely=0.75, relwidth=0.3, relheight=0.1)

blimpiar = Button(frame1,text='Limpiar',command=clean,bg='#A006BF',fg='white')
blimpiar.place(relx=0.55, rely=0.75, relwidth=0.3, relheight=0.1)





# bsalir = Button(frame1,text='Salir')
# bsalir.place(relx=0.3, rely=0.87, relwidth=0.3, relheight=0.1)

# frame2 = Frame(gui,border=1,bg='blue')
# frame2.config(width=200,height=200,relief='raised')
# frame2.grid(row=0,column=1)

# frame3 = Frame(gui,border=1,bg='green')
# frame3.config(width=200,height=200,relief='raised')
# frame3.grid(row=0,column=2)

# frame4 = Frame(gui,border=1,bg='black')
# frame4.config(width=200,height=200,relief='raised')
# frame4.grid(row=0,column=3)





gui.mainloop()


#gui.columnconfigure(tuple(range(3)), weight=1)   # CONFIGURAR GRID DE COLUMNAS  
#gui.rowconfigure(tuple(range(2)), weight=1)      # CONFIGURAR GRID DE FILAS 

# fonts=font.families()                           # FAMILIAS DE FONTS --LINEA 1
# print(fonts)                                    # FAMILIAS DE FONTS --LINEA 2
# OPCIONES RELIEF: 'groove','sunken','flat','raised','ridge'

# frame1 = Frame(gui,border=1)
# frame1.config(width='450' , height='300', relief='ridge',bg='red')
# frame1.place(x=25, y=80)

# frame2 = Frame(gui,border=1,bg='red')
# frame2.config(width='275' , height='300', relief='ridge')
# frame2.place(x=500, y=80)