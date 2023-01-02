from view import show_menu as ui
from database_r_w import read_database as read_db
from model import find_employee
from model import position_employee_selection
from model import salary_employee_selection
from database_r_w import add_employee
from database_r_w import del_employee
from database_r_w import upd_employee
from database_r_w import csv_data_export
from database_r_w import json_data_export


def controller():

    position = -1

    while position != 0:
        position = ui()
        data = read_db()
        match position:
            case 1:
                find_employee(data)
            case 2:
                position_employee_selection(data)
            case 3:
                salary_employee_selection(data)
            case 4:
                add_employee(data)
            case 5:
                del_employee(data)
            case 6:
                upd_employee(data)
            case 7:
                json_data_export(data)
            case 8:
                csv_data_export(data)
    else:
        print("конец работы")