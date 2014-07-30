__author__ = 'mark'

import sqlite3
import datetime

global db
db = db = "stasks.db"


def get_all_open_entries():
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    rows = cursor.execute("select * from tasks where done=0 order by insertTS DESC")
    connection.commit()
    entries = list()
    for row in rows:
        date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        inserted = date
        title = row[1]
        task_id = row[0]
        entries.append((title, inserted, task_id))
    return entries


def get_all_entries():
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    rows = cursor.execute("select * from tasks order by done, insertTS DESC")
    connection.commit()
    entries = list()
    for row in rows:
        done = row[3]
        date = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        inserted = date
        title = row[1]
        entries.append((title, inserted, done))
    return entries

def persist(title):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("insert into tasks(title) values (?)", [title])
    connection.commit()

def erase(task_id):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("update tasks set done=1 where id=?", [task_id])
    connection.commit()