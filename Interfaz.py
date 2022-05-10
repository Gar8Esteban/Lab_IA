import tkinter as tk
from tkinter.constants import LEFT, BOTTOM, TOP


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algoritmo')
        self.geometry('900x600')
        mainPanel = tk.Frame(self, width=900, height=600, bg='lightblue')
        mainPanel.pack(side=TOP)


if __name__ == '__main__':
    guide = gui()
    guide.mainloop()