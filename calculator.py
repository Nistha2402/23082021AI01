import tkinter as tkr
app=tkr.Tk(__name__)
app.title("MY GUI APP")
app.geometry("450x350")
num1=tkr.Variable(app)
num2=tkr.Variable(app)
output=tkr.Variable(app)
tkr.Entry(app,textvariable=num1).place(x=80,y=60)
tkr.Entry(app,textvariable=num2).place(x=290,y=60)
def func1():
    print(int(num1.get())+int(num2.get()))
    output.set(int(num1.get())+int(num2.get()))
def func2():
    print(int(num1.get())-int(num2.get()))
    output.set(int(num1.get())-int(num2.get()))
def func3():
    print(int(num1.get())*int(num2.get()))
    output.set(int(num1.get())*int(num2.get()))
def func4():
    print(int(num1.get())/int(num2.get()))
    output.set(int(num1.get())/int(num2.get()))
def func5():
    print(int(num1.get())**int(num2.get()))
    output.set(int(num1.get())**int(num2.get()))
tkr.Label(app, text="NUMBER1 : ").place(x=0,y=60)
tkr.Label(app, text="NUMBER2 : ").place(x=220,y=60)
tkr.Label(app, text="RESULT : ").place(x=150,y=260)
tkr.Label(app,textvariable=output).place(x=200,y=260)
tkr.Button(app,text="+",command=func1,width=2).place(x=180,y=160)
tkr.Button(app,text="-",command=func2,width=2).place(x=210,y=160)
tkr.Button(app,text="*",command=func3,width=2).place(x=240,y=160)
tkr.Button(app,text="/",command=func4,width=2).place(x=270,y=160)
tkr.Button(app,text="^",command=func5,width=2).place(x=300,y=160)
app.mainloop()
