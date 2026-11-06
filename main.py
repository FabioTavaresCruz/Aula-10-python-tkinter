import tkinter as tk

janela = tk.Tk()
janela.title("Login")
janela.configure(bg="white")
janela.geometry("800x600")


frame = tk.Frame(janela, bg="white", width=300, height=350)
frame.pack_propagate(False)
frame.pack(padx=150, pady=100)

img = tk.PhotoImage(file="imagem.png")
img_label = tk.Label(frame, image=img, bg="white")
img_label.pack(pady=20)

entry_box = tk.Entry(frame, text="email", width=30, bg="#EEEBEB", fg="black", bd=1, relief="raised", highlightthickness=0)
entry_box.pack(pady=10, ipady=8)


entry_box1 = tk.Entry(frame, text="senha", width=30, bg="#EEEBEB", fg="black", bd=1, relief="raised", highlightthickness=0)
entry_box1.pack(pady=3,ipady=8)


btn_login = tk.Label(frame, text="Acessar", bg="#298FC2", fg="white", width=30, height=2, bd=1, relief="raised", highlightthickness=0)
btn_login.pack(pady=8)

rotulo1 = tk.Label(frame, text="Primeiro acesso", bg="white", fg="#298FC2")
rotulo1.pack(pady=28)

janela.mainloop()
