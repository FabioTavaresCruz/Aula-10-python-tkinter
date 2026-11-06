import tkinter as tk


janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("400x300")


rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack()


janela.mainloop()
