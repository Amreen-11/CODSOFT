contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"{name} has been added to your contacts.")

def view_contact_list():
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    query = input("Enter a name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if query in name or query in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Contact found. Please enter new details:")
        phone = input("New phone number: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"{name}'s contact details have been updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact has been deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")