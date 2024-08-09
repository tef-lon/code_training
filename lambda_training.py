import tkinter as tk
import sys

main = tk.Tk()
main.geometry("300x600")

stack = 1

def show_win():
    global stack
    win = tk.Tk()
    win.geometry("200x100")
    stack += 1
    win.title("Fenster: {0}".format(stack))
    
    button4 = tk.Button(win, text="Beenden", command=lambda: win.destroy())
    button4.pack()

def add(stack):
    print(stack)
    stack = stack + 1
    print(stack)
    return stack 
    
def get_string(a, b):
    full_name = (a + " " + b)
    return full_name.title()

def change(wert):
    global stack
    stack = stack + wert
    print(stack)
    
s1 = "String1"
s2 = "String2"
print(s1 , s2)
print(s1 + s2)
print(s1 + str(2))

x = 1
y = 2
z = lambda x, y: x + y


print(get_string(".-@kurT", "bECKER"))
print("x=1")
print("y=2")
print(x,y)
print(x+y)
print("x und y", x, y)
print("y und y ", x, y, (x + y))




button1 = tk.Button(main, text="print to console", command=lambda: print("Guten Tag"))
button2 = tk.Button(main, text="Zweites Fenster", command=lambda: show_win())
button3 = tk.Button(main, text="Beenden", command=lambda: sys.exit())
button5 = tk.Button(main, text="stack +1", command=lambda: change(1))
button6 = tk.Button(main, text="stack -1", command=lambda: change(-1))

print(get_string("Bruder", "Schwester"))

button1.pack()
button2.pack()
button3.pack()
button5.pack()
button6.pack()

main.mainloop()

