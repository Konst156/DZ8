
def print_employee(employee):
    print('\nID: ', employee["id"], ' \nФамилия: ', employee["last_name"], ' \nИмя: ', employee["first_name"],
          ' \nномер телефона: ', employee['phone_num'], ' \nДолжность: ', employee['position'], ' \nЗарплата: ',
          employee['salary'])


def find_employee(data):
    search_value = input("Введите данные для поиска: Id, имя или фамилию: ")
    flag = 0
    for employee in data:
        if search_value == employee["id"] or search_value == employee["first_name"] or search_value == employee["last_name"]:
            print_employee(employee)
            flag = 1
            break
    if flag == 0:
        print ('\nтакого сотрудника нет')


def position_employee_selection(data):
    positions = []
    # отпределяем какие в принципе должности есть в нашей компании
    for employee in data:
        if not(employee['position'] in positions):
            positions.append(employee['position'])
    positions = list(enumerate(positions, 1))

    print(*positions, sep='\n' )
    pos_select = int(input(f'\n выберите должность, введите число от 1 до {len(positions)}: '))


    # выбираем сотрудников по указанной должности
    for employee in data:
        if employee['position'] == positions[pos_select-1][1]:
            print_employee(employee)

def salary_employee_selection(data):
    sal_min = float(input("введите минимальное значение заработной платы: "))
    sal_max = float(input("введите максимальное значение заработной платы: "))
    for employee in data:
        if sal_min <= float(employee['salary']) <= sal_max:
            print_employee(employee)
