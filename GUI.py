import Integracion as inte
import Interpolacion as inter
from tkinter import *
from sympy import *
from sympy import expand
x = Symbol('x')

#ventana para los metodos de interpolacion
def ventana1(a):
    def calcular():
        if(a==1):
            z,w,y=inter.diferencias(float(entradaR1.get()),float(entradaR2.get()),entry.get(),int(entry1.get()))
            res = inter.polnewtonsym(z,w)
            print(res)
            Label(ventana1, text=str(expand(res)), font=("Futura Md BT", 11), bg='RoyalBlue1').place(x=0, y=240)
            inter.graficar(w, y, expand(res), float(entradaR1.get()), float(entradaR2.get()), int(entry1.get()),entry.get())
        else:
            res,z,y = inter.MetodoLagrange2(float(entradaR1.get()),float(entradaR2.get()),entry.get(),int(entry1.get()))
            print(res)
            Label(ventana1, text=str(res), font=("Futura Md BT", 11), bg='RoyalBlue1').place(x=0, y=240)
            inter.graficar(z, y, res, float(entradaR1.get()), float(entradaR2.get()), int(entry1.get()),entry.get())

    ventana1 = Toplevel(ventana, bg="RoyalBlue1")
    ventana1.title("Interpolación")
    ventana1.geometry('350x300+610+10')
    if(a==1):
        Label(ventana1, text='Metodo de Newton', font=("Forte", 20, "bold"), bg='RoyalBlue1').pack()
    else:
        Label(ventana1, text='Metodo de Lagrange', font=("Forte", 20, "bold"), bg='RoyalBlue1').pack()

    Label(ventana1, text='Rango 1:',font=("Futura Md BT",14),bg="RoyalBlue1").place(x=0,y=60)
    entradaR1=StringVar()
    Entry(ventana1,textvariable=entradaR1,width=40).place(x=90,y=65)

    Label(ventana1, text='Rango 2:', font=("Futura Md BT", 14),bg="RoyalBlue1").place(x=0, y=115)
    entradaR2 = StringVar()
    Entry(ventana1, textvariable=entradaR2, width=40).place(x=90, y=120)


    Button(ventana1, text="CALCULAR", command=calcular,font=("Futura Md BT", 16), bg='slateGray3').place(x=90, y=165)

#ventana para los metodos de integracion
def ventana2(a):
    def calcular():
        if(a==1):
            res = inte.simpson(float(entradaR1.get()), float(entradaR2.get()), int(entry1.get()), entry.get())
            print(res)
            Label(ventana2, text='Resultado:', font=("Futura Md BT", 14), bg='RoyalBlue1').place(x=0, y=240) 
            Label(ventana2, text=str(round(res, 3)), font=("Futura Md BT", 14), bg='RoyalBlue1').place(x=150, y=240)      
        else:
            res = inte.trapecio(float(entradaR1.get()), float(entradaR2.get()), int(entry1.get()), entry.get())
            Label(ventana2, text='Resultado:', font=("Futura Md BT", 14), bg='RoyalBlue1').place(x=0, y=240) 
            Label(ventana2, text=str(round(res, 3)), font=("Futura Md BT", 14), bg='RoyalBlue1').place(x=150, y=240) 

    ventana2 = Toplevel(ventana, bg="RoyalBlue1")
    ventana2.title("Integracion")
    ventana2.geometry('350x300+610+10')
    if(a==1):
        Label(ventana2, text='Metodo de Simpson', font=("Forte", 20, "bold"), bg='RoyalBlue1').pack()
    else:
        Label(ventana2, text='Metodo del Trapecio', font=("Forte", 20, "bold"), bg='RoyalBlue1').pack()

    Label(ventana2, text='Rango 1:',font=("Futura Md BT",14),bg="RoyalBlue1").place(x=0,y=60)
    entradaR1=StringVar()
    Entry(ventana2,textvariable=entradaR1,width=40).place(x=90,y=65)

    Label(ventana2, text='Rango 2:', font=("Futura Md BT", 14),bg="RoyalBlue1").place(x=0, y=115)
    entradaR2 = StringVar()
    Entry(ventana2, textvariable=entradaR2, width=40).place(x=90, y=120)


    Button(ventana2, text="CALCULAR", command=calcular,font=("Futura Md BT", 16), bg='slateGray3').place(x=90, y=165)



#creamos la ventan principal
ventana = Tk()
ventana.geometry('400x460+100+100')
ventana.configure(background='yellow')
ventana.title("Interpolacion e Integracion")
titulo = Label(ventana, text='Interpolación e Integración',font=("Forte", 20, "bold"), bg='yellow')
titulo.pack()


Label(ventana, text='Función:', font=("Futura Md BT", 14), bg='yellow').pack(fill=X)
entry = Entry(ventana)
entry.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)
Label(ventana, text='Iteraciones', font=("Futura Md BT", 14), bg='yellow').pack(fill=X)
entry1 = Entry(ventana)
entry1.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)

Label(ventana, text='Interpolación', font=("Futura Md BT", 14), bg='yellow').pack(fill=X)
bt1=Button(ventana, text="Metodo de Newton", font=("Futura Md BT", 14), bg="black", width=34, fg="white")
bt1.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)
bt2=Button(ventana, text="Metodo de Lagrange", font=("Futura Md BT", 14), bg="black", width=34, fg="white")
bt2.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)
Label(ventana, text='Integración', font=("Futura Md BT", 14), bg='yellow').pack(fill=X)
bt3=Button(ventana, text="Metodo de Simpson", font=("Futura Md BT", 14), bg="black", width=34, fg="white")
bt3.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)
bt4=Button(ventana, text="Metodo del Trapecio", font=("Futura Md BT", 14), bg="black", width=34, fg="white")
bt4.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)

bt1.bind("<Button-1>", (lambda event: ventana1(1)))
bt2.bind("<Button-1>", (lambda event: ventana1(2)))

bt3.bind("<Button-1>",(lambda event: ventana2(1)))
bt4.bind("<Button-1>", (lambda event: ventana2(2)))

ventana.mainloop()
