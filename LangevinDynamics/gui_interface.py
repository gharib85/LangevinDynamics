import tkinter as tk
from tkinter import filedialog

global filename    
def gui(element,show):
    root = tk.Tk()
    elementList  = []
    labelList    = []
    for i in element:
        labelList.append(tk.Label(root, text=i))
        labelList[-1].pack()
        elementList.append(tk.Entry(root))
        elementList[-1].pack()
        
    a = tk.Button(root, text="browse file", width=10, command=lambda: select(elementList))
    a.pack()
    b = tk.Button(root, text="run", width=10, command=lambda:callback(elementList))
    b.pack()
    if show:
        tk.mainloop()
    return elementList,labelList        

def select(fname) :  # pragma: no cover
    vname = filedialog.askopenfilename(initialdir = "/",title = "Select file for potential")
    fname[-1].insert(0,vname)

def callback(element):  # pragma: no cover
    from tkinter import messagebox
    val = [] 
    go = True
    for i in element:
        val.append(i.get())
        if i.get() == "":
            messagebox.showinfo("Some values missing", "You are missing some input!!")
            go = False
            break
    if go :
        import LangevinDynamics as ld
        ld.run(float(val[0]),float(val[1])*float(val[2]),float(val[2]),float(val[3]),float(val[4]),val[-1],float(val[5]),int(val[6]),str(val[7]))
        messagebox.showinfo("Simulation Complete", "output saved as %s"%(val[7]))


def start():  # pragma: no cover
    element = ["x","v","m","Temperature","lambda","dt","steps","output filename","input filename"]
    gui(element,True)


