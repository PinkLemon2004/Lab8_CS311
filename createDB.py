import sqlite3
from tkinter import messagebox
from tkinter import *

def CreateDataBase():
    global conn , cursor
    conn = sqlite3.connect('activity/login.db')
    cursor = conn.cursor()
    sql = '''CREATE TABLE "Students" (
	"std_id"	INTEGER NOT NULL,
	"fist_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"score"	INTEGER NOT NULL DEFAULT 0,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("std_id")
)'''

CreateDataBase()