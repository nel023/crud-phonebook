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

def delete(contacts):
    deleteName = input("Enter name to be deleted: ")
    foundName = False
    for contact in contacts:
        if contact["name"].lower() == deleteName.strip().lower():
            contacts.remove(contact)
            foundName = True
            break
    
    if foundName == False:
        print("{} is not in the contacts.".format(deleteName)) 
    
    return contacts

def display(contacts):
    for i in contacts:
        print(i)

def search(contacts):
    searchName = input("Enter name to be search: ")
    foundSearchedName = False
    for contact in contacts:
        if contact["name"].lower() == searchName.strip().lower():
            print(contact)
            foundSearchedName = True        
            break
    
    if foundSearchedName == False:
        print("{} is not in the contacts.".format(searchName))

def update(contacts):
    pass

print("=========================")
print("Sample CRUD")
print("=========================\n")

while True:
    choose = input("\n[1]Add contacts\n[2]Delete contact/s\n[3]Display contacts\n[4]Search a contact\n[5]Update a contact\n[0]Exit\nChoose an option: \n")

    if choose == "1":
        add()
        
    elif choose == "2":
        delete(contacts)
        
    elif choose == "3":
        display(contacts)
        
    elif choose == "4":
        search(contacts)
        
    elif choose == "5":
        update()
        
    elif choose == "0":
        break
    
    else:
        print("\nWrong input, try again\n\n")
            
    




