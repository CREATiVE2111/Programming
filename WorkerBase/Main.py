import Registry_C as R
import Worker_C as W
mode = 1
while mode in [1, 2, 3, 4, 5, 6]:
    mode = int(input('Сhoose a use case:\n 1. Create tables\n 2. Adding an employee\n 3. Updating employee information\n 4. Output all employees of the company\n 5. View the table \n'))
    if mode == 1:
        R.Registry('crt', [])
    elif mode == 2:
        people_one = W.Worker()
        add_object = R.Registry('add', [people_one.name, people_one.company, people_one.start_date, people_one.end_date,
                                        people_one.post, people_one.salary])
    elif mode == 3:
        text = input('Сhangeable column, value, control column, condition \n')
        text = text.split(',')
        print(text)
        # upd_object = R.Registry('upd', ['start_date', 1898, 'name', 'Oleg Lebedev'])
        upd_object = R.Registry('upd', [text[0], text[1], text[2], text[3]])
    elif mode == 4:
        company = int(input('Choose a company: \n 1. RJD \n 2. Aeroflot \n 3. RUT \n 4. Gazprom \n 5. AvtoVAZ \n 6. X5_Group \n'))
        R.Registry('out', company)
    elif mode == 5:
        text = int(input('Choose a table: \n 1. job_registry \n 2. companies \n'))
        if text == 1:
            R.Registry('out_all', 'job_registry')
        elif text == 2:
            R.Registry('out_all', 'companies')
