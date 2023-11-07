# Bron:
# https://datatofish.com/executable-pyinstaller/
# 
# Om die program te vertaal:  Loop die volgende uit die Winpython shell
# pyinstaller --onefile hellowereld.py

import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def hello():
    label1 = tk.Label(
        root, text="Hallo Aarde!", fg="blue", font=("helvetica", 12, "bold")
    )
    canvas1.create_window(150, 200, window=label1)


button1 = tk.Button(text="Klik op my", command=hello, bg="brown", fg="white")
canvas1.create_window(150, 150, window=button1)

root.mainloop()