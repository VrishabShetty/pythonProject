from abc import ABC, abstractmethod
from tkinter import *

class NewWindow(ABC):

    @abstractmethod
    def get_master(self)-> Tk:
        pass

    def show_notification(self, text: str,)-> bool:
        try:
            notification = Toplevel(self.get_master())
            notification.title("Notification")
            Label(notification, text=text).grid(row=0, column=1, pady=30, padx=30)

            return True
        except:
            return False


