__author__ = 'mark'

from api import BaseInteraction
from Tkinter import *

class BasicListTaskInteraction(BaseInteraction.BaseInteraction):
    display_count = 6

    def add_containers(self, root):
        label_tuples = list()
        i = 0
        while i < self.display_count:
            container = LabelFrame(root, bd=0, height=2)
            container.grid(row=i, column=1, sticky=W)
            inserted_label = Label(container, justify=LEFT, anchor=W, width=55)
            inserted_label.pack(fill=X)
            title_label = Label(container, justify=LEFT, anchor=W, width=55)
            title_label.pack(fill=X)
            label_tuples.append((inserted_label, title_label))
            i += 1
        return label_tuples