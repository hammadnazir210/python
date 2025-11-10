import json
name=input("Enter your name: ")
phone=int(input("Enter your Phone Number: "))

with open("contact.json") as f:
    contact=json.load(f)

    contact [name]= phone

with open("contact.json" , "w") as f:
    json.dump(contact,f,indent=4)
   

    for key, value in contact.items():
        print(f" {key} : {value}")
