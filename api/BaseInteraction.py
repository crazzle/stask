__author__ = 'mark'

from Tkinter import *


# Base class for interactions, locks if
# there is already an executing interaction
class BaseInteraction(object):

    # Interaction logic to be implemented
    def execute(self):
        raise NotImplementedError()

    # Hotkey that interaction will be registered for
    def get_hotkey(self):
        raise NotImplementedError()

    # We need a runner because we don't want to challenge TKInter with Threads...
    def on_key_execute(self):
        raise NotImplementedError()

    # Initializes the TkInter-Window
    @staticmethod
    def initialize_window(title):
        root = Tk()
        root.title(title)
        root.resizable(0, 0)
        root.attributes("-topmost", True)
        return root

    # Lets user interact with TkInter-Window
    @staticmethod
    def let_interact(root):
        root.iconify()
        root.update()
        root.deiconify()
        root.mainloop()