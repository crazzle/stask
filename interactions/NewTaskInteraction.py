__author__ = 'mark'

from api import BaseInteraction
from Tkinter import *
from helper import dbhelper


class NewTaskInteraction(BaseInteraction.BaseInteraction):
    def execute(self):
        root = self.initialize_window("New Task")

        t = Text(root, height=2, width=50)
        t.pack(side=LEFT, fill=Y)
        t.focus_set()

        def save_and_dispose(event):
            title = event.widget.get("0.0", END)
            title = str(title).strip()
            dbhelper.persist(title)
            root.destroy()

        t.bind('<Return>', save_and_dispose)

        self.let_interact(root)

    def get_hotkey(self):
        return ['Shift', 'Alt', '1']