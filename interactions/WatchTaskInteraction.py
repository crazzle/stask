__author__ = 'mark'

from api import BaseInteraction
from Tkinter import *
import sqlite3
import datetime

class WatchTaskInteraction(BaseInteraction.BaseInteraction):
    begin = 0
    end = 5

    def re_init_vars(self):
        self.begin = 0
        self.end = 5

    @staticmethod
    def get_all_entries():
        connection = sqlite3.connect("stasks.db")
        cursor = connection.cursor()
        rows = cursor.execute("select * from tasks order by done, insertTS DESC")
        connection.commit()
        entries = list()
        for row in rows:
            done = row[3]
            date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
            inserted = date
            title = row[1]
            entries.append((title, inserted, done))
        return entries

    def execute(self):
        root = self.initialize_window("Watch Tasks")
        entries = self.get_all_entries()

        def dispose(event):
            root.destroy()

        def move_down(event):
            if self.end + 1 < len(entries):
                self.begin += 1
                self.end += 1
            show(self.begin, self.end)

        def move_up(event):
            if self.begin - 1 >= 0:
                self.begin -= 1
                self.end -= 1
            show(self.begin, self.end)

        all = set()
        def show(begin, end):
            for container in all:
                container.grid_remove()
            all.clear()
            i = 0
            for entry in entries:
                if (i >= begin) and (i <= end):
                    done = entry[2]
                    color = "black"
                    if done == 1:
                        color = "grey"
                    container = LabelFrame(root, bd=0, bg="grey", height=2)
                    inserted = entry[1]
                    inserted_label = Label(container, text=inserted, fg=color, justify=LEFT, anchor=W, width=55)
                    inserted_label.pack(fill=X)
                    title = entry[0]
                    if len(title) > 50:
                        title = title[:51]
                        title += "..."
                    title_label = Label(container, text=title, fg=color, justify=LEFT, anchor=W, width=55)
                    title_label.pack(fill=X)
                    container.grid(row=i, column=1, sticky=W)
                    all.add(container)
                i += 1

        root.bind('<Return>', dispose)
        root.bind('<w>', move_up)
        root.bind('<s>', move_down)

        show(self.begin, self.end)
        self.let_interact(root)
        self.re_init_vars()

    def get_hotkey(self):
       return ['Shift', 'Alt', '2']