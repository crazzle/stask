from interactions import EraseTaskInteraction, NewTaskInteraction, WatchTaskInteraction
from libs import pyhk
import sqlite3

__author__ = 'keinmark'


# Initialize the database on startup if
# app is started first time
def initialize_db():
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


# Starting the control flow
initialize_db()

# Create instances of interactions
newTaskInteraction = NewTaskInteraction.NewTaskInteraction()
watchTaskInteraction = WatchTaskInteraction.WatchTaskInteraction()
eraseTaskInteraction = EraseTaskInteraction.EraseTaskInteraction()

#create pyhk class instance
hot = pyhk.pyhk()

#add hotkey
hot.addHotkey(newTaskInteraction.get_hotkey(), newTaskInteraction.on_key_execute)
hot.addHotkey(watchTaskInteraction.get_hotkey(), watchTaskInteraction.on_key_execute)
hot.addHotkey(eraseTaskInteraction.get_hotkey(), eraseTaskInteraction.on_key_execute)

#start looking for hotkey.
hot.start()