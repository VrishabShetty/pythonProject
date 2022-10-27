from tkinter import *
import tkinter as tk
from tkinter import messagebox
from AbtractNewWindowClass import NewWindow
from BrakeCalculator import BrakeCalculator

class PressureInCylinder(NewWindow):

    _window: Tk = None
    _master: Tk = None

    def setCalculator(self, calculator: BrakeCalculator):
        self._calculator = calculator

    def setMaster(self, master: Tk):
        self._master = master
        self._window = tk.Toplevel(master)
        self._window.title("Brake Force And Torque")

    def show(self):
        Label(self._window, text="Enter the Pedal Ratio:").grid(row=0, column=0, padx=30, pady=10)
        prn = Entry(self._window, width=5, borderwidth=5)
        prn.grid(row=0, column=1, pady=10)
        Label(self._window, text=":").grid(row=0, column=2, padx=10, pady=10)
        prd = Entry(self._window, width=5, borderwidth=5)
        prd.grid(row=0, column=3, pady=10)

        Label(self._window, text="Enter the Pedal Force(Fpl):").grid(row=1, column=0, padx=30, pady=10)
        fP = Entry(self._window, width=50, borderwidth=5)
        fP.grid(row=1, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Radius of Master Cylinder:").grid(row=2, column=0, padx=30, pady=10)
        d = Entry(self._window, width=50, borderwidth=5)
        d.grid(row=2, column=1, padx=30, pady=10)

        Label(self._window, text="Enter the Radius of :").grid(row=3, column=0, padx=30, pady=10)
        r = Entry(self._window, width=50, borderwidth=5)
        r.grid(row=3, column=1, padx=30, pady=10)

        def calculate():
            pMC, fDisc, bT = self._calculator.pressure_master_cylinder(float(prn.get())/float(prd.get()),
                                                                       float(fP.get()), float(d.get()),
                                                                       float(r.get()))

            text = "Pressure in Master Cyclinder is {pmc:.2f}\n\nBreak Force is {fForce:.2f} && Breaking Torque is {fTor:.2f}\n\n\n" \
            .format(fForce=fDisc, fTor=bT, pmc=pMC)

            if messagebox.showinfo("Answer", text):
                self._window.destroy()

        next_btn = Button(self._window, text="Next", command=calculate)
        next_btn.grid(row=4, column=1, pady=20)

    def get_master(self)-> Tk:
        return self._window

