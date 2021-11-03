from tkinter import *
from tkinter import ttk

from fractions import Fraction
from gauss import gauss_init
from gauss_jordan import gssjrdn
from inversa import inversa
from cramer import cramer

root = Tk()
root.title("Algebra Lineal - Ecuaciones Lineales, Luis Daniel Derma Rios 3BSist")

frame = LabelFrame(root, text = 'Matriz por: ', font=('Arial', 15))
frame.grid(row = 0, column = 0, columnspan = 3, pady = 20 )

var = IntVar()
var.set(1)
#buttons
Radiobutton(frame, text="Gauss", variable=var, value=1, font=('Arial', 15), activebackground="#F6D55C").grid(row = 1, column=0)
Radiobutton(frame, text="Gauss-Jordan", variable=var, value=2, font=('Arial', 15) , activebackground="#F6D55C").grid(row = 1, column=1)
Radiobutton(frame, text="Inversa", variable=var, value=3, font=('Arial', 15) , activebackground="#F6D55C").grid(row = 1, column=2)
Radiobutton(frame, text="Carmer", variable=var, value=4, font=('Arial', 15), activebackground="#F6D55C").grid(row = 1, column=3)


rangeR = int(input("Numero de Incognitas: "))

if(rangeR > 10): rangeR = 3;

## configurar tamano
if(rangeR <= 4):
    root.geometry("700x700")
else:
    root.geometry("1200x700")
        
# listas intermediarias
matrixEntries = []
resultEntries= []

matrixValues = []
resultValues= []

# recibe los datos en cada 'calcular'
def fetchData():
    matrixValues.clear()
    resultValues.clear()
    
    for x in resultEntries:
        if "/" in x.get():
            resultValues.append(Fraction(int(x.get().split("/")[0]),int(x.get().split("/")[1])))
        else:            
            resultValues.append(x.get())
        
    for i in range(0, rangeR):
        matrixValues.append([])
        for r in matrixEntries[i]:
            if "/" in r.get():
                matrixValues[i].append(Fraction(int(r.get().split("/")[0]),int(r.get().split("/")[1])))
            else:            
                matrixValues[i].append(r.get())
            
    process_data()

# operaciones: Value button, matrixValues, resultValues, 
def process_data():
    count = 0
    if(var.get() == 1):
        print("Metodo por: Guass")
        sol = gauss_init(matrixValues,resultValues)
        
    elif (var.get() == 2):
        print("Metodo por: Guass-Jordan")
        sol = gssjrdn(matrixValues,resultValues)
        
    elif (var.get() == 3): 
        print("Metodo por: Inversa")
        sol = inversa(matrixValues,resultValues)
        print(sol, "SOL")
    elif (var.get() == 4):
        print("Metodo por: Cramer")
        sol = cramer(matrixValues,resultValues)
    print("Solucion")
    for s in sol:
        print(Fraction(s).limit_denominator())
            
    solution = LabelFrame(root, text = 'Solucion: ', font=('Arial', 15))
    solution.grid(row = 1, column = 0, columnspan = 3, pady = 20 )
    
    for r in range(0, rangeR):
        for c in range(0, 2):
            solu = Entry(solution, width=10, font=('Arial', 20))
            solu.grid(padx=5, pady=5, row=r, column=c)
            if(c == 0):
                solu.insert(0,"X{}".format(r+1))
            else:
                solu.insert(0,Fraction(sol[r]).limit_denominator())
                count += 1


# imprime la matriz, crea variables 
for r in range(0, rangeR):
    matrixEntries.append([])
    for c in range(0, rangeR+1):
        str = "cell{}{}".format(r, c)    
        locals()[str] = Entry(frame, width=10, font=('Arial', 15))
        locals()[str].grid(padx=5, pady=5, row=r+2, column=c)
        if(c == rangeR):            
            locals()[str].insert(0, 'R{}'.format(r+1))
            resultEntries.append(locals()[str])
        else:            
            locals()[str].insert(0, 'X{}'.format(c+1))
            matrixEntries[r].append(locals()[str])
        


boton = Button(frame, text="Calcular", command=fetchData, font=('Arial', 15))
boton.grid()

root.mainloop()