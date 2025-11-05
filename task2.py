import json

try:
    # read file
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError)
    contacts = {}

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
        print("new file ban gyi {}")



name=input("Enter your Name: ")
phone=int(input("Enter your phone number: "))

with open("week2\contacts.json") as f:
    contacts=json.load(f)

    contacts[name]=phone

with open("week2\contacts.json ","w") as f:
    json.dump(contacts,f,indent=4)

    for key, value in contacts.items():
        print(f"{key} : {value}")   
