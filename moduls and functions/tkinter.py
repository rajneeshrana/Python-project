try:
    import tkinter
except importError:  #python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.TK()

mainWindow.title("Hello World")
mainWindow.geometry('640x480')
mainWindow.mainloop()
