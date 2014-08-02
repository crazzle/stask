__author__ = 'mark'

import BasicListTaskInteraction
from helper import dbhelper
import subprocess


class WatchTaskInteraction(BasicListTaskInteraction.BasicListTaskInteraction):
    begin = 0
    end = 5
    display_count = 6

    def on_key_execute(self):
        subprocess.Popen("python .\\runner\WatchTaskRunner.py")

    def re_init_vars(self):
        self.begin = 0
        self.end = 5

    def execute(self):
        root = self.initialize_window("Watch Tasks")
        label_tupels = self.add_containers(root)
        entries = dbhelper.get_all_entries()

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

        def show(begin, end):
            i = 0
            container_index = 0
            for entry in entries:
                if (i >= begin) and (i <= end):
                    done = entry[2]
                    color = "black"
                    if done == 1:
                        color = "darkgreen"

                    bgcolor = "white"
                    if i % 2 == 0:
                        bgcolor = "lightblue"

                    labels = label_tupels[container_index]

                    inserted = entry[1]
                    inserted_label = labels[0]
                    inserted_label.configure(text=inserted)
                    inserted_label.configure(fg=color)
                    inserted_label.configure(bg=bgcolor)

                    title = entry[0]
                    if len(title) > 50:
                        title = title[:51]
                        title += "..."
                    title_label = labels[1]
                    title_label.configure(text=title)
                    title_label.configure(fg=color)
                    title_label.configure(bg=bgcolor)

                    container_index += 1
                i += 1
            root.update()

        def self_destroy(event):
            root.destroy()

        root.bind('<Return>', dispose)
        root.bind('<w>', move_up)
        root.bind('<s>', move_down)
        root.bind('<Escape>', self_destroy)

        show(self.begin, self.end)
        self.let_interact(root)
        self.re_init_vars()

    def get_hotkey(self):
       return ['Shift', 'Alt', '2']