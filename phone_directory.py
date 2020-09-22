print("Welcome to the Phone Directory")
#Dictionary for storing names and numbers
directory = {}

#function for adding a new name and number
def add_entry(name, number):
    if name in directory:
        print("Name already exists in directory.")
    else:
        directory[name] = number
        print("Successfully added entry!")
        return
    
#function for looking up a number by name
def lookup_number(name):
    if name in directory:
        print(f"Name: {name}, Number: {directory[name]}")
    else:
        print("Name does not exist.")
        return False

#Infinite loop so the program keep running
while True:
    print("-----")
    print("If you would like to add an entry, type 'add'")
    print("If you would like to lookup a name, type 'lookup'")
    
    command = input("> ")

    #Conditional logic to parse the command entered by user
    if command == "add":
        name = input("Please enter a name > ")
        number = input ("Please enter a number > ")
        add_entry(name, number)
    elif command == "lookup":
        name = input("Please enter a name to lookup > ")
        lookup_number(name)
    else: #Send error message for invalid commands
        print("Sorry, I do not recognize this command")
