from tkinter import Tk
from tkinter import ttk
import sys


class Tela_Calc:

    # criando construtor
    def __init__(self):
        self.janela_calc = Tk()
        self.config_janela_calc()
        self.janela_calc.mainloop()
    
    def config_janela_calc(self):
        self.janela_calc.geometry('300x300')
        self.janela_calc.title("Amor Calc")
        self.janela_calc.resizable(False, False)
        self.janela_calc.configure(background='#fff')




if __name__ == "__main__":
    calc = Tela_Calc()
    