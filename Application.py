__author__ = 'keinmark'

#!/usr/bin/env python
from Tkinter import *
import sqlite3
import EraseTasks
import NewTask
import WatchTasks

def initializeDb():
    connection = sqlite3.connect("stasks.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title varchar(255) NOT NULL,
      insertTS TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      done INTEGER DEFAULT 0,
      doneTS TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    connection.commit()

initializeDb()

root = Tk()
root.title("Stasks")
root.resizable(0, 0)
root.geometry("500x500")
root.focus_set()
root.bind('<Control-N>', NewTask.newTask)
root.bind('<Control-W>', WatchTasks.watchTasks)
root.bind('<Control-E>', EraseTasks.eraseTask)
root.mainloop()