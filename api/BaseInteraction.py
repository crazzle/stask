__author__ = 'mark'

from Tkinter import *


# Base class for interactions, locks if
# there is already an executing interaction
class BaseInteraction(object):

    # Indicates if an interaction implementation is currently executing
    global closed
    closed = True

    # Interaction logic to be implemented
    def execute(self):
        raise NotImplementedError()

    # Hotkey that interaction will be registered for
    def get_hotkey(self):
        raise NotImplementedError()

    # Invoked by hotkey, controls the locking
    def on_key_execute(self):
        if self.is_closed():
            self.open()
            self.execute()
            self.close()

    # Close when an interaction is finished
    @staticmethod
    def close():
        global closed
        closed = True

    # Open when an interaction is going to be executed
    @staticmethod
    def open():
        global closed
        closed = False

    # Check if any interaction is currently executing
    @staticmethod
    def is_closed():
        global closed
        return closed

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