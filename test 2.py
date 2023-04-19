# create an empty dictionary to store phone directory
phoneDirectory = {}

# define a function to add a record
def add_record():
    name = input("Enter name: ")
    phone = input("Enter your 10-digit phone number: ")
    phoneDirectory[name] = phone
    print("Record added")

# define a function to search a record
def search_record():
    name = input("Enter name to search: ")
    if name in phoneDirectory:
        print(name + ": " + phoneDirectory[name])
    else:
        print("Record not found")

# define a function to update a record
def update_record():
    name = input("Enter name: ")
    if name in phoneDirectory:
        phone = input("Enter new 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record updated")
    else:
        print("Record not found")

# define a function to delete a record
def delete_record():
    name = input("Enter name: ")
    if name in phoneDirectory:
        del phoneDirectory[name]
        print("Record deleted")
    else:
        print("Record not found")

# main program loop
while True:
    print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        search_record()
    elif choice == '3':
        update_record()
    elif choice == '4':
        delete_record()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
