from tkinter import *
import tkinter as tk
from tkinter import messagebox
from AbtractNewWindowClass import NewWindow
from BrakeCalculator import BrakeCalculator

class Loads(NewWindow):

    _window: Tk = None
    _master: Tk = None

    def setCalculator(self, calculator: BrakeCalculator):
        self._calculator = calculator

    def setMaster(self, master: Tk):
        self._master = master
        self._window = tk.Toplevel(master)
        self._window.title("Weight Transfer")


    def show(self):
        Label(self._window, text="Enter the Height of centre of gravity(H):").grid(row=0, column=0, padx=30, pady=10)
        h = Entry(self._window, width=50, borderwidth=5)
        h.grid(row=0, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Wheel of Base(L):").grid(row=1, column=0, padx=30, pady=10)
        l = Entry(self._window, width=50, borderwidth=5)
        l.grid(row=1, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Mass(W):").grid(row=2, column=0, padx=30, pady=10)
        w = Entry(self._window, width=50, borderwidth=5)
        w.grid(row=2, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Front Load:").grid(row=3, column=0, padx=30, pady=10)
        fL = Entry(self._window, width=50, borderwidth=5)
        fL.grid(row=3, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Rear Load:").grid(row=4, column=0, padx=30, pady=10)
        rL = Entry(self._window, width=50, borderwidth=5)
        rL.grid(row=4, column=1, padx=30, pady=10)

        def calculate():
            self._calculator.weight_transfer(int(h.get()), float(l.get()), int(w.get()))
            self._calculator.dynamic_load(float(fL.get()),float(rL.get()))
            text = "Weight Transfer is {value:.2f}\n\n\nDynamic Load:\n\nFront is {front:.2f} && Rear is {rear:.2f}"\
                .format(value=self._calculator.wT,front=self._calculator.wD[0],rear=self._calculator.wD[1])

            if messagebox.showinfo("Answer", text):
                self._window.destroy()

        next_btn = Button(self._window, text="Next", command=calculate)
        next_btn.grid(row=6, column=1, pady=20)


    def get_master(self)-> Tk:
        return self._window
