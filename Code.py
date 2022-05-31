import tkinter as tk #GUI
import numpy as np #Array calc
from tabulate import tabulate #table the data
from scipy.misc import derivative #for derivative
import matplotlib.pyplot as plt #for Graph plotting
from math import *

formula = '' #input formula
newton=True #method choice
error=True  #error or iteration
error_value= 0.0001 #default error
iteration_value= 10 #default iterations
#it_max=100
num1=0 #initial guess
num2=0 #initial guess

Data=[] #Data array
inputInfo = [['**', 'for power'], ['*', 'for multiply'], ['/', 'for division'], ['+', 'for addition'], ['-', 'for subtraction'], ['x', 'for variable'], ['exp()', 'for exponential'], ['sqrt()','for square root'], ['pow()','for power']] #input info array

def fd(x):
    fd = derivative(f,x,0.00001,1)
    return fd


def f(x):
    f = eval(formula, {'exp': exp, 'sqrt': sqrt, 'pow': pow, 'cos': cos, 'sin': sin, 'tan': tan, 'x': x})
    return f

def Secant():

    i = 1
    global num1,num2,error,Data, error_value,iteration_value
    while True:
        if f(num2) != f(num1):
            num3 = num2 - (f(num2) * (num2 - num1)) / (f(num2) - f(num1))
            errorCalc = abs(num3 - num2)
        Data=np.append(Data,[i,num1,f(num1),num2,f(num2),num3,f(num3),errorCalc])
        i += 1
        num1 = num2
        num2 = num3
        if error and errorCalc < error_value:
            break
        elif not error and i > iteration_value:
            break
    print(Data)
    Data.shape=(i-1,8)

def Newton():

    i = 1
    global num1, num2, error, Data, error_value, iteration_value
    while True:
        if fd(num1) != 0:
            num2 = num1 - f(num1) / fd(num1)
            errorCalc = abs(num2 - num1)
        Data=np.append(Data,[i,num1,f(num1),fd(num1),num2,f(num2),errorCalc])
        i += 1
        num1 = num2
        if error and errorCalc < error_value:
            break
        elif not error and i > iteration_value:
            break
    print(Data)
    Data.shape = (i-1, 7)


def getf(entry):
    global formula
    formula = entry
    print(formula)
    frame.destroy()
    showframe2()

def getChoice(fl):
    global newton
    newton = fl
    if newton:
        print('n')
    else:
        print('s')
    frame2.destroy()
    showframe3()

def getError(e):
    global error,error_value
    error_value = e
    error = True
    print(e)
    frame3.destroy()
    if newton:
        showframeN()
    else:
        showframeS()

def getIter(i):
    global error,iteration_value
    iteration_value = i
    error = False
    print(i)
    frame3.destroy()
    if newton:
        showframeN()
    else:
        showframeS()

def getSecant(n1,n2):
    global num1,num2
    num1=n1
    num2=n2
    print(n1)
    print(n2)
    frameS.destroy()
    root.destroy()

def getNewton(n):
    global num1
    num1=n
    print(n)
    frameN.destroy()
    root.destroy()

def showGraph():
    root2.destroy()
    plt.plot(Data_it, Data_error)
    plt.title('Output Error')
    plt.ylabel('Error')
    plt.xlabel('Iteration')
    plt.show()

def SaveData():
    f = open("Data.txt", "w+")
    f.write(table)
    f.close()

def showInfo():
    rootInfo = tk.Tk()
    rootInfo.title("Input Information")
    rootInfo.geometry('400x250')
    #rootInfo.eval('tk::PlaceWindow . center')

    mytext = tk.Text(rootInfo, width=100, height=50)
    mytext.pack(pady=20)
    mytext.insert('end', tabulate(inputInfo))

    rootInfo.mainloop()

def showframe1():
    frame.place(relwidth=1, relheight=1, relx=0.5, rely=0, anchor='n')

    fun_info = tk.Label(frame, text='enter F(x)', bg=default_color, font=("Arial", 20))
    fun_info.place(relwidth=0.7, relheight=0.1, relx=0.1, rely=0.3)

    label_fun = tk.Label(frame, text='F(x)', bg=default_color, font=("Arial", 20))
    label_fun.place(relwidth=0.25, relheight=0.1, relx=0, rely=0.4)

    entry_fun = tk.Entry(frame, font=("Arial", 20))
    entry_fun.place(relwidth=0.6, relheight=0.1, relx=0.2, rely=0.4)

    button = tk.Button(frame, text='Enter', font=("Arial", 20), command=lambda: getf(entry_fun.get()))
    button.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.55)

    info_button = tk.Button(frame, text='info', font=('Arial', 16), command=lambda: showInfo())
    info_button.place(relwidth=0.1, relheight=0.1, relx=0.7, rely=0.3, anchor='w')

def showframe2():
    frame2.place(relwidth=1, relheight=1, relx=0.5, rely=0, anchor='n')

    secantB = tk.Button(frame2, text='Secant', font=("Arial", 25), command=lambda: getChoice(False))
    secantB.place(relwidth=0.35, relheight=0.1, relx=0.1, rely=0.5)

    newtonB = tk.Button(frame2, text='Newton', font=("Arial", 25), command=lambda: getChoice(True))
    newtonB.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.5)

    fun_info = tk.Label(frame2, text='Select Secant or Newton', bg=default_color, font=("Arial", 25) )
    fun_info.place(relwidth=0.7, relheight=0.1, relx=0.1, rely=0.3)

def showframe3():
    frame3.place(relwidth=1, relheight=1, relx=0.5, rely=0, anchor='n')

    errorButton = tk.Button(frame3, text='enter Error', font=("Arial", 18), command=lambda: getError(float(error_entry.get())))
    errorButton.place(relwidth=0.35, relheight=0.1, relx=0.1, rely=0.6)

    error_entry = tk.Entry(frame3, font=("Arial", 18), justify= 'center')
    error_entry.place(relwidth=0.35, relheight=0.1, relx=0.1, rely=0.45)

    iteration = tk.Button(frame3, text='enter It.', font=("Arial", 18), command=lambda: getIter(int(iteration_entry.get())))
    iteration.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.6)

    iteration_entry = tk.Entry(frame3, font=("Arial", 18), justify= 'center')
    iteration_entry.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.45)

    fun_info = tk.Label(frame3, text='Enter Error limit or No. of iterations:', bg=default_color, font=("Arial", 18))
    fun_info.place(relwidth=0.7, relheight=0.1, relx=0.1, rely=0.3)

def showframeS():
    frameS.place(relwidth=1, relheight=1, relx=0.5, rely=0, anchor='n')

    button = tk.Button(frameS, text='enter', font=("Arial", 18), command=lambda: getSecant(float(entry1.get()),float(entry2.get())))
    button.place(relwidth=0.4, relheight=0.1, relx=0.45, rely=0.6, anchor='n')

    entry1 = tk.Entry(frameS, font=("Arial", 25), justify= 'center')
    entry1.place(relwidth=0.35, relheight=0.1, relx=0.1, rely=0.45)

    entry2 = tk.Entry(frameS, font=("Arial", 25), justify='center')
    entry2.place(relwidth=0.35, relheight=0.1, relx=0.5, rely=0.45)

    fun_info = tk.Label(frameS, text='Enter two initial values', bg=default_color, font=("Arial", 25))
    fun_info.place(relwidth=0.7, relheight=0.1, relx=0.1, rely=0.3)

def showframeN():
    frameN.place(relwidth=1, relheight=1, relx=0.5, rely=0, anchor='n')

    button = tk.Button(frameN, text='enter', font=("Arial", 18), command=lambda: getNewton(float(entry.get())))
    button.place(relwidth=0.3, relheight=0.1, relx=0.45, rely=0.6, anchor='n')

    entry = tk.Entry(frameN, font=("Arial", 25), justify='center')
    entry.place(relwidth=0.35, relheight=0.1, relx=0.45, rely=0.45, anchor='n')

    fun_info = tk.Label(frameN, text='Enter the initial value', bg=default_color, font=("Arial", 25))
    fun_info.place(relwidth=0.7, relheight=0.1, relx=0.1, rely=0.3)

#print(f(4))
#print(fd(4))

Height = 400
Width = 600
default_color = '#2596be'

root = tk.Tk()
root.title('Numerical Methods Project')

canvas = tk.Canvas(root,height=Height,width=Width)
canvas.pack()
frame = tk.Frame(root, bg=default_color)
frame2 = tk.Frame(root, bg=default_color)
frame3 = tk.Frame(root, bg=default_color)
frameS = tk.Frame(root, bg=default_color)
frameN = tk.Frame(root, bg=default_color)

showframe1()

root.mainloop()

if newton:
    Newton()
    print(tabulate(Data, headers=['i', 'num1', 'f(num1)', 'fd(num1)', 'num2', 'f(num2)', 'error']))
    table = tabulate(Data, headers=['i', 'num1', 'f(num1)', 'fd(num1)', 'num2', 'f(num2)', 'error'])
else:
    Secant()
    #Data=np.round(Data,4)
    print(tabulate(Data,headers=['i','num1','f(num1)','num2','f(num2)','num3','f(num3)','error']))
    table=tabulate(Data,headers=['i','num1','f(num1)','num2','f(num2)','num3','f(num3)','error'])
#D_it=Data[:,0]
#Dnum1=Data[:,1]
#Dnum1f=Data[:,2]
#Dnum2=Data[:,3]
#Dnum2f=Data[:,4]
#Dnum3=Data[:,5]
#Dnum3f=Data[:,6]
Data_error=Data[:,-1]
Data_it=Data[:,0]



root2 = tk.Tk()
root2.title('Data')

mytext=tk.Text(root2, width=100, height=35)
mytext.pack(pady=20)
mytext.insert('end',table)

outputLabel= tk.Label(root2, text='Best Estimate', font=("Arial", 12))
outputLabel.pack(pady=20)

outputText= tk.Text(root2, width=20, height=2, font=("Arial", 12))
outputText.insert('end', round(num2,6))
outputText.pack(pady=20)


GraphButton= tk.Button(root2, text='Error Graph', font=("Arial", 18), command=lambda: showGraph())
GraphButton.pack(pady=20, side='left', ipadx=40, padx=30)

SaveButton= tk.Button(root2, text='Save Data', font=("Arial", 18), command=lambda: SaveData())
SaveButton.pack(pady=20, side='right', ipadx=40, padx=30)


root2.mainloop()