phone_directory = {}

def add_contact() :
    name = input("Enter name: ")
    if name in phone_directory:
        print("name already exist")
    else:
        number = int(input("Enter Number: "))
        phone_directory[name] = number
        print("contact added successfully")

def delete_contact():
    name = input("Enter the name of "
                "contact to be deleted: ")
    if name in phone_directory:
        phone_directory.pop(name) 
        print("Contact Deleted Successfully!")
    else:
        print("No such contact found")

def search():
    name = input("Search for a "
                 "contact by name: ")
    if name in phone_directory.keys():
        print("Number is",phone_directory[name])
    else:
        print("Name not found.")
    
def update_contact():
    old_name = input("Enter the current name: ")
    new_number = int(input("Enter the "
                           "updated number: "))
    if old_name in phone_directory.keys():
        phone_directory[old_name] = new_number
        print("Contact Updated Successfully!")
    else:
        print("No such contact found")

def display_contact():
    print("\n\nPhone Directory:\n")
    for name, number in phone_directory.items():
        print(name, ": ",number)

while True:
    print(
            "\n1. Add Contact \n"
            "2. Delete Contact \n"
            "3. Search Contact\n"
            "4. Update Contact\n"
            "5. Display All Contacts\n"
            "6. Quit\n"
    )

    option = int(input("Choose an option: "))

    if option == 1:
        add_contact()
    elif option == 2:
        delete_contact()
    elif option == 3:
        search()
    elif option == 4:
        update_contact()
    elif option == 5:
        display_contact()
    elif option == 6:
        break
    else:
        print("Invalid Option")

