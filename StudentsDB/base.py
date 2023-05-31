import sqlite3
import tabulate
import student as stud_proc
table = [['id', 'name', 'department', 'starting_year', 'mark1', 'mark2', 'mark3', 'status']]

def create():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student (
                  student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  department TEXT NOT NULL,
                  starting_year INT NOT NULL,
                  mark1 FLOAT NOT NULL,
                  mark2 FLOAT NOT NULL,
                  mark3 FLOAT NOT NULL,
                  status TEXT NOT NULL
                );""")
    con.commit()
    con.close()
    print("Table was created")

def drop():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("""DROP TABLE student""")
    con.commit()
    con.close()
    print("Table was deleted")

def output(req):
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute(req)
    output = cur.fetchall()
    con.close()
    print("Data was output")
    return output

switch = int(input())

if switch != 0:
    switch = int(input())
    stud_proc.insert(int(switch))
else:
    switch = input()
    if switch == 'otc':
        stud_proc.otchislenie()
    if switch == 'cre':
        create()
    if switch == 'drop':
        drop()
    if switch == 'all':
        all = output("SELECT * FROM student")
        for i in all:
            table.append(i)
        print(tabulate.tabulate(table, tablefmt="simple_grid", stralign='center'))