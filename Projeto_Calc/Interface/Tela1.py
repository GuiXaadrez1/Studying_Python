from tkinter import Tk
from tkinter import ttk
import awesometkinter as atk  # vai ser necessário renomear os frames que tem a class Frame



class Tela_Calc:

    # criando construtor
    def __init__(self):
        self.janela_calc = Tk()
        self.config_janela_calc()
        self.janela_calc.mainloop()
    
    def config_janela_calc(self):
        self.janela_calc.geometry('300x400')
        self.janela_calc.title("Amor Calc")
        self.janela_calc.resizable(False, False)
        self.janela_calc.configure(background='#DA70D6')
        self.frames()
        self.widgets_frame2()

    def frames(self):
        # primeira Frame, aqui vai aparecer os cálculos e os resultados
        self.frame1 = ttk.Frame(self.janela_calc)
        self.frame1.place(relx='0.035',rely='0.05',relwidth='0.92',relheight='0.15')
    
        # segundo Frame, vamos colocar os botões 
        self.frame2 = ttk.Frame(self.janela_calc)
        self.frame2.place(relx='0.035',rely='0.25',relwidth='0.92',relheight='0.72')
        
    def widgets_frame2(self):
        bt1 = ttk.Button(self.frame2,text='C')
        bt1.place(relx=0.01, rely=0.02, relwidth=0.2, relheight=0.15)
        bt2 = ttk.Button(self.frame2,text='M1')
        bt2.place(relx=0.21, rely=0.02, relwidth=0.2, relheight=0.15)
        pass    
        
        
         



if __name__ == "__main__":
    calc = Tela_Calc()
    