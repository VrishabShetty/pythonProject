from tkinter import *
from tkinter import messagebox
from BrakeCalculator import BrakeCalculator
from BrakeForceAndTorque import BrakeForceAndTorque
from Loads import Loads
from PressureInCylinder import PressureInCylinder

calculator = BrakeCalculator()
itr = 0


def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()


def next_btn():
    global itr
    if itr == 0:
        loads = Loads()
        loads.setMaster(root)
        loads.setCalculator(calculator)
        loads.show()
        msg.configure(text="Calculating Weight Transfer...")
        itr += 1
    elif itr == 1:
        BFT = BrakeForceAndTorque()
        BFT.setMaster(root)
        BFT.setCalculator(calculator)
        BFT.show()
        msg.configure(text="Calculating Brake Force and Torque...")
        itr += 1
    elif itr == 2:
        PIN = PressureInCylinder()
        PIN.setMaster(root)
        PIN.setCalculator(calculator)
        PIN.show()
        msg.configure(text="Calculating Pressure In Cylinder...")
        itr += 1



root: Tk = Tk()
text = "Welcome to World"
msg = Message(root, text=text, padx=30, pady=20)
msg.config(bg='lightgreen', font=('times', 25, 'italic'))
msg.pack()

next_btn = Button(root, text="Next", command=next_btn)
next_btn.pack(pady=20)

root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()
