#Simple Phonebook

import csv

contactInfo = {}
fName = ""
lName = ""
number = ""
contacts = []

contactsFile = "contacts.csv"

def add(contactsFile):
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    number = input("Enter number: ")
    newContact = {
        "name": fName + " " + lName,
        "number": int(number)
    }
          
    with open(contactsFile, mode="a", newline="") as csv_file:
        # Define the CSV writer
        fieldnames = newContact.keys()  # Use the keys from the new_item as fieldnames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # If the file is empty, write the header row
        if csv_file.tell() == 0:
            writer.writeheader()

        # Write the new item as a row
        writer.writerow(newContact)
        
def display(contactsFile):
    with open(contactsFile, mode="r", newline="") as csv_file:
        reader =csv.DictReader(csv_file)
        for row in reader:
            print(row)

def search(contactsFile):
    searchName = input("Enter name to be search: ")
    foundSearchedName = False
    for contact in contacts:
        if contact["name"].lower() == searchName.strip().lower():
            print(contact)
            foundSearchedName = True        
            break
    
    if foundSearchedName == False:
        print("{} is not in the contacts.".format(searchName))

def update(contactsFile):
    pass

def delete(contactsFile):
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


print("=========================")
print("Sample CRUD")
print("=========================\n")

while True:
    choose = input("\n[1]Add contacts\n[2]Delete contact/s\n[3]Display contacts\n[4]Search a contact\n[5]Update a contact\n[0]Exit\nChoose an option: \n")

    if choose == "1":
        add(contactsFile)
        
    elif choose == "2":
        delete(contactsFile)
        
    elif choose == "3":
        display(contactsFile)
        
    elif choose == "4":
        search(contactsFile)
        
    elif choose == "5":
        update(contactsFile)
        
    elif choose == "0":
        break
    
    else:
        print("\nWrong input, try again\n\n")
            
    




