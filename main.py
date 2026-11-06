import tkinter as tk


janela = tk.Tk()
janela.title("Login")
janela.configure(bg="white")
janela.geometry("400x300")


rotulo = tk.Label(janela, text="Login")
rotulo.pack()


entry_box = tk.Entry(janela, width=30)
entry_box.pack()

janela.mainloop()
