from tkinter import *
import tkinter as tk
from tkinter import messagebox
from AbtractNewWindowClass import NewWindow
from BrakeCalculator import BrakeCalculator

class BrakeForceAndTorque(NewWindow):

    _window: Tk = None
    _master: Tk = None

    def setCalculator(self, calculator: BrakeCalculator):
        self._calculator = calculator

    def setMaster(self, master: Tk):
        self._master = master
        self._window = tk.Toplevel(master)
        self._window.title("Brake Force And Torque")

    def show(self):
        Label(self._window, text="Enter the Radius of Wheel(Rw):").grid(row=0, column=0, padx=30, pady=10)
        rw = Entry(self._window, width=50, borderwidth=5)
        rw.grid(row=0, column=1, padx=30, pady=10)

        def calculate():
            self._calculator.brakingForce()
            self._calculator.brakingTorque(float(rw.get()))

            text = "Front:\n\nBreak Force is {fForce:.2f} && Breaking Torque is {fTor:.2f}\n\n\n" \
                   "Rear:\n\nBreak Force is {rForce:.2f} && Breaking Torque is {rTor:.2f}" \
                .format(fForce=self._calculator.bF[0], fTor=self._calculator.bT[0],
                        rForce=self._calculator.bF[1], rTor=self._calculator.bT[1])

            if messagebox.showinfo("Answer", text):
                self._window.destroy()

        next_btn = Button(self._window, text="Next", command=calculate)
        next_btn.grid(row=2, column=1, pady=20)

    def get_master(self)-> Tk:
        return self._window
