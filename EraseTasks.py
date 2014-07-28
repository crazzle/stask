__author__ = 'keinmark'

from Tkinter import *
import sqlite3
import datetime

def eraseTask(event):
    root = Tk()
    root.title("Watch Task")
    root.resizable(0, 0)
    connection = sqlite3.connect("stasks.db")
    cursor = connection.cursor()
    rows = cursor.execute("select * from tasks where done=0 order by insertTS DESC")
    connection.commit()

    entries = set()
    for row in rows:
        date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        inserted = date
        title = row[1]
        id = row[0]
        entries.add((title, inserted, id))

    global begin
    begin = 0
    global end
    end = 5
    global chosen
    chosen = 0
    global id
    id = -1

    def eraseAndDispose(event):
        connection = sqlite3.connect("stasks.db")
        cursor = connection.cursor()
        cursor.execute("update tasks set done=1 where id=?", [id])
        connection.commit()
        root.destroy()

    def moveDown(event):
        global end
        global begin
        global chosen
        if (chosen == end) and (end + 1 < len(entries)):
            begin += 1
            end += 1
        if chosen < len(entries)-1:
            chosen += 1
        show(begin, end, chosen)

    def moveUp(event):
        global end
        global begin
        global chosen
        if (chosen == begin) and (begin - 1 >= 0):
            begin -= 1
            end -= 1
        if chosen > 0:
            chosen -= 1
        show(begin, end, chosen)

    all = set()
    def show(begin, end, chosen):
        global id
        for container in all:
            container.grid_remove()
        all.clear()
        i = 0
        for entry in entries:
            if (i >= begin) and (i <= end):
                color = "black"
                if chosen == i:
                    color = "blue"
                    id = entry[2]
                container = LabelFrame(root, bd=0, bg="grey", height=2)
                inserted = entry[1]
                insertedLabel = Label(container, text=inserted, fg=color, justify=LEFT, anchor=W, width=55)
                insertedLabel.pack(fill=X)
                title = entry[0]
                if len(title) > 50:
                    title = title[:51]
                    title += "..."
                titleLabel = Label(container, text=title, fg=color, justify=LEFT, anchor=W, width=55)
                titleLabel.pack(fill=X)
                container.grid(row=i, column=1, sticky=W)
                all.add(container)
            i += 1


    root.bind('<Return>', eraseAndDispose)
    root.bind('<w>', moveUp)
    root.bind('<s>', moveDown)

    show(begin, end, chosen)