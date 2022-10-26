from input_data import add_contact_csv, add_contact_txt
from import_export import read_contacts_csv, find_contact_csv, read_contacts_txt, find_contact_txt


def run_menu():
    flag = True
    while flag:
            print("1 - Find contact (csv)")
            print("2 - Add contact(csv)")
            print("3 - Show all contacts(csv)")
            print("4 - Find contact (txt)")
            print("5 - Add contact(txt)")
            print("6 - Show all contacts(txt)")
            print("7 - Exit")
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("!!Please, select 1, 2, 3, 4, 5, 6, 7!!\n")
                continue
            if choice == "1": 
                find_contact_csv()
                break
            elif choice == "2":
                add_contact_csv()
                break
            elif choice == "3":
                read_contacts_csv()
            elif choice == "4":
                find_contact_txt()
                break
            elif choice == "5":
                add_contact_txt()
                break
            elif choice == "6":
                read_contacts_txt()
            else: 
                flag = False
                break