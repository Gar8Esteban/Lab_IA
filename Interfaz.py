import tkinter as tk
from tkinter import Tk, Frame, Canvas, filedialog, messagebox, Scale, Button
from tkinter.constants import ALL, HORIZONTAL


class Guide(tk.Tk):
    def __int__(self):
        super().__init__()
        self.title('Draw')


if __name__ == '__main__':
    guide = Guide()
    guide.mainloop()
