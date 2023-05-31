import sqlite3
import random as rd

def generation():
    names = ['Alexey', 'Oleg', 'Ivan', 'Anton', 'Nikita', 'Andrey', 'Kirill']
    surname = ['Smirnov', 'Petrov', 'Ivanov', 'Lebedev', 'Sidorov', 'Vinogradov', 'Morozov']
    department = ['IT', 'DataAnalytics', 'Designer', 'Economist', 'SysAdmin']
    year = [2017, 2018, 2019, 2020, 2021, 2022]
    mark = [1, 2, 3, 4, 5]
    status = ['accepted', 'expelled']
    return str(rd.choice(names) + ' ' +rd.choice(surname)), rd.choice(department), rd.choice(year),\
           rd.choice(mark), rd.choice(mark), rd.choice(mark), status[0]

def insert(count):
    for i in range(count):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO student ("
                    f"name, department, starting_year, mark1, mark2, mark3, status) VALUES (?, ?, ?, ?, ?, ?, ?);", generation())
        con.commit()
        con.close()
    print(f"{count} students were added")

def otchislenie():
    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE ((mark1 + mark2 + mark3)/3)  < 3.5")
    con.commit()
    con.close()
    print(f"Students were expelled")