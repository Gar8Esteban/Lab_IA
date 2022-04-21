from tkinter import Tk, Frame, Canvas, filedialog, messagebox, Scale, Button
from tkinter.constants import ALL, HORIZONTAL

from PIL import ImageGrab

if __name__ == '__main__':
    lineX = 0
    lineY = 0
    color = 'black'

    def linexy(event):
        global lineX
        global lineY
        lineX = event.x
        lineY = event.y

    def line(event):
        global lineX
        global lineY
        canvas.create_line((lineX, lineY, event.x, event.y), fill=color, width=espesor.get())
        lineX = event.x
        lineY = event.y

    def farbeAndern(newcolor):
        global color
        color = newcolor

    def loschen():
        global color
        color = 'white'

    def sauber():
        canvas.delete(ALL)

    def aus():
        root.destroy()
        root.quit()

    def zeichnungSpeichern():
        try:
            fileName = filedialog.asksaveasfilename(defaultextension='.png')

            x = root.winfo_rootx() + canvas.winfo_x()
            y = root.winfo_rooty() + canvas.winfo_y()

            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()

            ImageGrab.grab().crop((x, y, x1, y1)).save(fileName)
            messagebox.showinfo('Guardar dibujo', 'Guardado en: '+str(fileName))
        except:
            messagebox.showerror('Guardar dibujo', 'Error al guardar. ')


    root = Tk()
    root.state('zoomed')
    root.config(bg='black')
    root.title('Draw')

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    frame = Frame(root, bg='black', height=200)
    frame.grid(column=0, row=0, sticky='ew')
    frame.columnconfigure(0, minsize=200, weight=1)

    canvas = Canvas(root, height=660, bg='white')
    canvas.grid(column=0, row=1, sticky='nsew')
    canvas.rowconfigure(0, weight=1)
    canvas.columnconfigure(0, minsize=100, weight=1)
    canvas.bind('<Button-1>', linexy)
    canvas.bind('<B1-Motion>', line)

    canvasColores = Canvas(frame, bg='black', width=5, height=40)
    canvasColores.grid(column=0, row=0, sticky='ew', padx=1, pady=1)

    id = canvasColores.create_rectangle((10, 10, 30, 30), fill='red')
    canvasColores.tag_bind(id, '<Button-1>', lambda x: farbeAndern('red'))

    id = canvasColores.create_rectangle((40, 10, 60, 30), fill='blue')
    canvasColores.tag_bind(id, '<Button-1>', lambda x: farbeAndern('blue'))

    id = canvasColores.create_rectangle((70, 10, 90, 30), fill='orange')
    canvasColores.tag_bind(id, '<Button-1>', lambda x: farbeAndern('orange'))

    id = canvasColores.create_rectangle((100, 10, 120, 30), fill='black')
    canvasColores.tag_bind(id, '<Button-1>', lambda x: farbeAndern('black'))

    espesor = Scale(frame, orient=HORIZONTAL, from_=0, to=50, length=200, relief='groove', bg='gold', width=17,
                    sliderlength=20, highlightbackground='white', activebackground='red')
    espesor.set(1)
    espesor.grid(column=1, row=0, sticky='ew', padx=2, pady=1)

    guardar = Button(frame, text='Guardar', bg='green', command=zeichnungSpeichern, width=10, height=2,
                     activeforeground='white', font=('comic sens MS', 10, 'bold'))
    guardar.grid(column=2, row=0, sticky='ew', pady=1, padx=4)

    borrar = Button(frame, text='Borrar', bg='orange', command=loschen, width=10, height=2,
                     activeforeground='white', font=('comic sens MS', 10, 'bold'))
    borrar.grid(column=3, row=0, sticky='ew', pady=1, padx=4)

    limpiar = Button(frame, text='Limpiar', bg='red', command=sauber, width=10, height=2,
                     activeforeground='white', font=('comic sens MS', 10, 'bold'))
    limpiar.grid(column=4, row=0, sticky='ew', pady=1, padx=4)

    salir = Button(frame, text='Salir', bg='red', command=aus, width=10, height=2,
                     activeforeground='white', font=('comic sens MS', 10, 'bold'))
    salir.grid(column=5, row=0, sticky='ew', pady=1, padx=4)

    root.mainloop()