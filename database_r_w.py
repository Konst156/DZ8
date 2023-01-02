import csv
import json

def read_database():

    db_list = []
    with open("database.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter = ";")
        for row in reader:
            db_list.append(row)

    return db_list

def write_database(data, path = "database.csv"):

    with open(path, "w", encoding='utf-8') as csvfile:
        fieldnames = ['id', 'last_name', 'first_name', 'phone_num', 'position', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ";", lineterminator ="\n")
        writer.writeheader()
        for employee in data:
            writer.writerow({'id':employee['id'], 'last_name':employee['last_name'], 'first_name': employee['first_name'], 'phone_num': employee['phone_num'], 'position':employee['position'], 'salary': employee['salary']})

def id_read():
    with open('db_id.txt','r') as file:
        id = int(file.readline())
    return id    

def id_write(id):
    with open('db_id.txt','w') as file:
        file.write(str(id))

def add_employee(data):
    id_count = id_read()
    for employee in data:
        if int(employee['id'])>id_count:
            id_count = int(employee['id'])

    new_employee={}
    new_employee['id'] = str(id_count+1)
    new_employee['last_name']= input("введите фамилию сотрудника: ")
    new_employee['first_name'] = input("введите имя сотрудника: ")
    new_employee['phone_num'] = input("введите номер телефона сотрудника: ")
    new_employee['position'] = input("введите должность сотрудника: ")
    new_employee['salary'] = input("введите зарплату сотрудника: ")

    data.append(new_employee)

    write_database(data)
    id_write(id_count)

def del_employee(data):
    id_del = input("введите ID сотрудника для удаления записи: ")
    flag = 0
    for employee in data:
        if id_del == employee['id']:
            flag = 1
            data.remove(employee)
            print("сотрудник удален")
            write_database(data)
            break
    if flag == 0:
        "сотрудник стаким ID не найден"



def upd_employee(data):
    id_upd = input("введите ID сотрудника для изменения данных: ")
    flag = 0
    for employee in data:
        if id_upd == employee['id']:
            flag = 1

            field = input("введите номер поля для изменения: 1-фамилия, 2-имя, 3-номер телефона, 4-должность, 5-зарплата: ")

            match field:
                case "1":
                    employee['last_name']=input('введите новую фамилию:')
                case "2":
                    employee['first_name']=input('введите новое имя: ')
                case "3":
                    employee['phone_num']=input('введите новвый номер телефона: ')
                case "4":
                    employee['position']=input('введите новую должность: ')
                case "5":
                    employee['salary']=input('введите новую зарплату: ')
                case _:
                    print("ошибка ввода")

            write_database(data)
            print("\n данные обновлены")
            break
    if flag==0:
        "сотрудник с таким ID не найден"

def csv_data_export(data):
    path_to_export = input("введите имя файла для экспорта даныйх в формате .csv: ") + '.csv'

    write_database(data, path_to_export)

def json_data_export(data):
    path_to_export = input("введите имя файда для экспорта даныйх в формате json: ") + '.json'

    with open(path_to_export, 'w', encoding='utf-8') as file:
        for employee in data:
            json.dump(employee, file, ensure_ascii=False, indent=4)