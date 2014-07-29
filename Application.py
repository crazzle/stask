from interactions import EraseTasks, WatchTasks, NewTask
from libs import pyhk
import sqlite3

__author__ = 'keinmark'

global closed
closed = True

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

def openNewTask():
   openInteraction(NewTask.newTask)

def openWatchTask():
    openInteraction(WatchTasks.watchTasks)

def openEraseTask():
    openInteraction(EraseTasks.eraseTask)

def openInteraction(interaction):
    global closed
    if closed:
        closed = False
        interaction()
        closed = True

initializeDb()

#create pyhk class instance
hot = pyhk.pyhk()

#add hotkey
hot.addHotkey(['Shift', 'Alt', '1'], openNewTask)
hot.addHotkey(['Shift', 'Alt', '2'], openWatchTask)
hot.addHotkey(['Shift', 'Alt', '3'], openEraseTask)

#start looking for hotkey.
hot.start()