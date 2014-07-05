__author__ = 'keinmark'

#!/usr/bin/env python
from Tkinter import *
import sqlite3

def newTask(event):
    print "hallo"

def watchTasks(event):
    print "hallo"

def oldTask(event):
    print "hallo"

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

initializeDb()

root = Tk()
root.title("Whois Tool")
root.resizable(0, 0)
root.geometry("500x500")
root.bind('<Control-N>', newTask)
root.bind('<Control-W>', newTask)
root.bind('<Control-O>', newTask)
root.mainloop()