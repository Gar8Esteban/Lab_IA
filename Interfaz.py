import tkinter as tk


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algoritmo')


if __name__ == '__main__':
    guide = gui()
    guide.mainloop()