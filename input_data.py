from import_export import write_contact_csv, write_contact_txt 
import menu


def add_contact_csv():
    print("Add new contact:")
    flag = True
    while flag:
        surname = input("Enter surname: ")
        phone_num = input("Enter phone number: ")
        write_contact_csv(surname, phone_num)
        flag = False
    menu.run_menu()

def add_contact_txt():
    print("Add new contact:")
    flag = True
    while flag:
        surname = input("Enter surname: ")
        phone_num = input("Enter phone number: ")
        write_contact_txt(surname, phone_num)
        flag = False
    menu.run_menu()
        
