
#encoding: utf-8

import tkinter as tk

class LabelWindow(tk.Tk):
    def __init__(self, title=''):
        super().__init__()

        label = tk.Label(self, text=title, bg="red", fg="yellow", pady=10)

        label.pack(side=tk.TOP, fill=tk.X)


if __name__ == "__main__":
    label = LabelWindow("label")
    label.geometry("400x600")
    label.mainloop()






