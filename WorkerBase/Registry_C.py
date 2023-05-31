import sqlite3

class Registry:
    def __init__(self, mode, inf):
        self.names = ['Alexey', 'Oleg', 'Ivan', 'Anton', 'Nikita', 'Andrey', 'Kirill', 'Andrey']
        if mode == 'crt':
            self.create1()
            self.create2()
        elif mode == 'add':
            self.add(inf)
        elif mode == 'upd':
            self.upd(inf)
        elif mode == 'out':
            self.out(inf)
        elif mode == 'out_all':
            self.output_all(inf)

    def create1(self):
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS companies (
                       company TEXT NOT NULL,
                       info TEXT NOT NULL
                    );""")
        con.commit()
        con.close()
        self.add_com()

    def create2(self):
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS job_registry (
                       name TEXT NOT NULL,
                       company TEXT NOT NULL,
                       start_date TEXT NOT NULL,
                       end_date TEXT,
                       post TEXT NOT NULL,
                       salary FLOAT NOT NULL
                    );""")
        con.commit()
        con.close()

    def add(self, inf):
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        cur.execute(f"INSERT INTO job_registry (name, company, start_date, end_date, post, salary) "
                    f"VALUES (?, ?, ?, ?, ?, ?);",
                    [inf[0], inf[1], inf[2], inf[3], inf[4], inf[5]])
        con.commit()
        con.close()



    def add_com(self):
        company = ['RJD', 'Aeroflot', 'RUT', 'Gazprom', 'AvtoVAZ', 'X5_Group']
        info = ['The best company', 'The safest and most comfortable flights',\
                'The best transport institute in the country', 'Best gas', 'The best cars', 'The freshest products']
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        for i in range (len(info)):
            cur.execute(f"INSERT INTO companies (company, info) "
                    f"VALUES (?, ?);",
                    [company[i], info[i]])
        con.commit()
        con.close()

    def upd(self, inf):
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        print(f"UPDATE job_registry SET {inf[0]} = '{inf[1]}' WHERE {inf[2]} = '{inf[3]}'")
        cur.execute(f"UPDATE job_registry SET {inf[0]} = {inf[1]} WHERE {inf[2]} = '{inf[3]}'")
        con.commit()
        con.close()

    def out(self, inf):
        company = ['RJD', 'Aeroflot', 'RUT', 'Gazprom', 'AvtoVAZ', 'X5_Group']
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        print(company[inf-1])
        cur.execute(f"SELECT name FROM job_registry gr "
                    f"JOIN companies cm on gr.company = cm.company "
                    f"WHERE cm.company = '{company[inf-1]}'")
        text = cur.fetchall()
        print(text)

    def output_all(self, table):
        con = sqlite3.connect("company.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table}")
        text = cur.fetchall()
        n = 1
        for i in text:
            print(n, i)
            n+=1