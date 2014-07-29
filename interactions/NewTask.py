__author__ = 'keinmark'

from Tkinter import *
import sqlite3


def newTask():
    root = Tk()
    root.title("New Task")
    root.resizable(0, 0)
    root.attributes("-topmost", True)

    t = Text(root, height=2, width=50)
    t.pack(side=LEFT, fill=Y)
    t.focus_set()

    def saveAndDispose(event):
        title = event.widget.get("0.0",END)
        title = str(title).strip()
        connection = sqlite3.connect("stasks.db")
        cursor = connection.cursor()
        cursor.execute("insert into tasks(title) values (?)", [title])
        connection.commit()
        root.destroy()

    t.bind('<Return>', saveAndDispose)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()