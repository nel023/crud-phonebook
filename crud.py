#Simple Phonebook

contacts = []
fName = ""
lName = ""
number = ""

def add():
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    number = input("Enter number: ")
    contacts.append({"name":fName + " " +lName, "number":int(number)})
    return contacts

def delete():
    for i in range(len(contacts)):
        deleteName = input("Enter name to be deleted: ")
        if contacts[i]["name"].lower() == deleteName.strip().lower():
            contacts.pop(i)
            print("Contact succesfully deleted.")
            break
        else:
            print("Wrong name/contact name does not exists.")
            break

def display(contacts):
    for i in contacts:
        print(i)

def search():
    pass

def update():
    pass

print("=========================")
print("Sample CRUD")
print("=========================\n")

while True:
    choose = input("\nPress the following:\n[1]Add contacts\n[2]Delete contact/s\n[3]Display contacts\n[4]Search a contact\n[5]Update a contact\n[0]Exit\n")

    if choose == "1":
        add()
        
    elif choose == "2":
        delete()
        
    elif choose == "3":
        display(contacts)
        
    elif choose == "4":
        search()
        
    elif choose == "5":
        update()
        
    elif choose == "0":
        break
    
    else:
        print("\nWrong input, try again\n\n")
            
    




