__author__ = 'mark'

from api import BaseInteraction
from Tkinter import *
from helper import dbhelper


class EraseTaskInteraction(BaseInteraction.BaseInteraction):

    begin = 0
    end = 5
    chosen = 0
    task_id = -1

    def re_init_vars(self):
        self.begin = 0
        self.end = 5
        self.chosen = 0
        self.task_id = -1

    def execute(self):
        root = self.initialize_window("Erase Tasks")
        entries = dbhelper.get_all_open_entries()

        def erase_and_dispose(event):
            dbhelper.erase(self.task_id)
            root.destroy()

        def move_down(event):
            if (self.chosen == self.end) and (self.end + 1 < len(entries)):
                self.begin += 1
                self.end += 1
            if self.chosen < len(entries)-1:
                self.chosen += 1
            show(self.begin, self.end, self.chosen)

        def move_up(event):
            if (self.chosen == self.begin) and (self.begin - 1 >= 0):
                self.begin -= 1
                self.end -= 1
            if self.chosen > 0:
                self.chosen -= 1
            show(self.begin, self.end, self.chosen)

        all = set()

        def show(begin, end, chosen):
            for container in all:
                container.grid_remove()
            all.clear()
            i = 0
            for entry in entries:
                if (i >= begin) and (i <= end):
                    color = "black"
                    if chosen == i:
                        color = "blue"
                        self.task_id = entry[2]
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

        root.bind('<Return>', erase_and_dispose)
        root.bind('<w>', move_up)
        root.bind('<s>', move_down)

        show(self.begin, self.end, self.chosen)
        self.let_interact(root)
        self.re_init_vars()

    def get_hotkey(self):
        return ['Shift', 'Alt', '3']