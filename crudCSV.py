#Simple Phonebook

import csv

contactInfo = {}
fName = ""
lName = ""
number = ""

contactsFile = "contacts.csv"

def add(contactsFile):
    fName = input("Enter first name: ")
    lName = input("Enter last name: ")
    number = input("Enter number: ")
    newContact = {
        "name": fName + " " + lName,
        "number": int(number)
    }
          
    with open(contactsFile, mode="a", newline="") as csv_file:      # Define the CSV writer
        fieldnames = newContact.keys()      # Use the keys from the new_item as fieldnames
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:        # If the file is empty, write the header row
            writer.writeheader()

        writer.writerow(newContact)     # Write the new item as a row

def delete(contactsFile, deleteName):
    data = []
    foundName = False
    
    with open(contactsFile, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for contact in reader:
            data.append(contact)
            
    newData = []
    for row in data:
        if row["name"].strip().lower() != deleteName.strip().lower():
            newData.append(row)
        else:
            foundName = True
            
    if foundName:
        with open(contactsFile, mode="w", newline="") as file:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(newData)
    
    return foundName
       
def display(contactsFile):
    with open(contactsFile, mode="r", newline="") as csv_file:
        reader =csv.DictReader(csv_file)
        for row in reader:
            print(row)
        
def search(contactsFile):
    searchName = input("Enter name to be search: ")
    foundSearchedName = False
    with open(contactsFile, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
    
        for contact in reader:
            if contact["name"].lower() == searchName.strip().lower():
                print(contact)
                foundSearchedName = True
                break
    
    if foundSearchedName == False:
        print("{} is not in the contacts.".format(searchName))

def update(contactsFile):
    data = []
    updateName = input("Enter contact name to be update: ")
    foundUpdateName = False
    with open(contactsFile, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for contact in reader:
            data.append(contact)
            
    newData = []
    for row in data:
        if row["name"].strip().lower() != updateName.strip().lower():
            newData.append(row)
        else:
            foundUpdateName = True
    
    

print("=========================")
print("Sample CRUD")
print("=========================\n")

while True:
    choose = input("\n[1]Add contacts\n[2]Delete contact/s\n[3]Display contacts\n[4]Search a contact\n[5]Update a contact\n[0]Exit\nChoose an option: \n")

    if choose == "1":
        add(contactsFile)
        
    elif choose == "2":
        deleteName = input("Enter name to be deleted: ")
        value = delete(contactsFile, deleteName)
        if value:
            print("{} was successfully deleted in contacts.".format(deleteName))
        else:
            print("{} is not in the contacts.".format(deleteName))
             
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
            
    




