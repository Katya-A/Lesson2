job = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(job)):
    str_name = job[i].split(" ")
    name_i = len(str_name) -1
    sp_name = str_name[name_i]
    name = sp_name.lower().title()
    job.append(name)
    print(f"Привет, {name}, добро пожаловать")