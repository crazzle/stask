__author__ = 'keinmark'

from Tkinter import *
import sqlite3
import datetime

def watchTasks(event):
    root = Tk()
    root.title("Watch Task")
    screenResY = root.winfo_screenheight()
    root.geometry("200x100")# + str(screenResY))
    root.resizable(0, 0)

    vscrollbar = Scrollbar(root)
    vscrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(root, yscrollcommand=vscrollbar.set)
    canvas.pack(side=LEFT, fill=Y)

    vscrollbar.config(command=canvas.yview)

    # make the canvas expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    #
    # create canvas contents
    frame = Frame(canvas)
    frame.rowconfigure(1, weight=2)
    frame.columnconfigure(1, weight=1)

    connection = sqlite3.connect("stasks.db")
    cursor = connection.cursor()
    rows = cursor.execute("select * from tasks order by done ASC, insertTS DESC")
    connection.commit()

    for row in rows:

        done = row[3]
        color = "black"
        if(done == 1):
            color = "grey"

        container = LabelFrame(frame, bd=2)

        date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        inserted = date
        insertedLabel = Label(container, text=inserted, fg=color, justify=LEFT, anchor=W)
        insertedLabel.pack(fill=X)

        title = row[1]
        titleLabel = Label(container, text=title, fg=color, justify=LEFT, anchor=W)
        titleLabel.pack(fill=X)

        container.pack(fill=X)

    canvas.create_window(0, 0, anchor=NW, window=frame)

    frame.update_idletasks()

    canvas.config(scrollregion=canvas.bbox("all"))

    def dispose(event):
        root.destroy()

    root.bind('<Return>', dispose)