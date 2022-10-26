
def write_contact_csv(sn, p_num):
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.csv')
    with open(path, "a", encoding="UTF-8") as f:
        f.write(f"{sn}, {p_num};\n")


def read_contacts_csv():
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.csv')
    with open(path, "r", encoding="UTF-8") as f: 
        print(f.read())


def find_contact_csv():
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.csv')
    sn = input("Enter surname: ")
    with open(path, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if line.startswith(sn):
                print("Found:\n", line)        


def write_contact_txt(sn, p_num):
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.txt')
    with open(path, "a", encoding="UTF-8") as f:
        f.write(f"{sn}, {p_num};\n")


def read_contacts_txt():
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.txt')
    with open(path, "r", encoding="UTF-8") as f: 
        print(f.read())


def find_contact_txt():
    path = ('C:\\Users\\Asus\\Downloads\\GeekBrains\\Projects\\Phone_book\\book.txt')
    sn = input("Enter surname: ")
    with open(path, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            if line.startswith(sn):
                print("Found:\n", line)        