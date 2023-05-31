import random as rd

class Worker:
    def __init__(self):
        inf = self.generation()
        self.name = inf[0]
        self.company = inf[1]
        self.start_date = inf[2]
        self.end_date = inf[3]
        self.post = inf[4]
        self.salary = inf[5]

    def generation(self):
        names = ['Alexey', 'Oleg', 'Ivan', 'Anton', 'Nikita', 'Andrey', 'Kirill', 'Andrey']
        surnames = ['Smirnov', 'Petrov', 'Ivanov', 'Lebedev', 'Sidorov', 'Vinogradov', 'Morozov','Mikhailov']
        company = ['RJD', 'Aeroflot', 'RUT', 'Gazprom', 'AvtoVAZ', 'X5_Group']
        year_s = [1990, 1992, 1994, 1996, 1998, 2000]; year_e = [2020, 2022, 2024, 2026, 2028, 2020, None]
        post = ['IT', 'DataAnalytics', 'Designer', 'Economist', 'SysAdmin', 'Director', 'Secretary']
        salary = [45000, 67000, 83000, 100000, 129000]
        return str(rd.choice(names) + '_' + rd.choice(surnames)), rd.choice(company), rd.choice(year_s), \
            rd.choice(year_e), rd.choice(post), rd.choice(salary)