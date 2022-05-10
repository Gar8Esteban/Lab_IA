import tkinter as tk
from tkinter.constants import LEFT, BOTTOM, TOP


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algoritmo')
        self.geometry('900x600')
        mainPanel = tk.Frame(self, width=900, height=600, bg='lightblue')
        mainPanel.grid(row=0, column=0)

        labelName1 = tk.Label(mainPanel, text='Esteban García Ochoa-1803291', bg='lightblue')
        labelName1.grid(row=0, column=0)

        labelName2 = tk.Label(mainPanel, text='Duvan José Botia-18032xx', bg='lightblue')
        labelName2.grid(row=0, column=1)

        labelXi = tk.Label(mainPanel, text='Xi', bg='lightblue')
        labelXi.grid(row=1, column=0)

        entryXi = tk.Entry(mainPanel)
        entryXi.grid(row=1, column=1)

        labelXf = tk.Label(mainPanel, text='Xf', bg='lightblue')
        labelXf.grid(row=2, column=0)

        entryXf = tk.Entry(mainPanel)
        entryXf.grid(row=2, column=1)

        buttonEntry = tk.Button(mainPanel, text='Ingresar', bg='green')
        buttonEntry.grid(row=3, column=0)

        buttonDelete = tk.Button(mainPanel, text='Borrar', bg='red')
        buttonDelete.grid(row=3, column=1)


if __name__ == '__main__':
    guide = gui()
    guide.mainloop()