import json

# Function to load data from file
def load_data():
    try:
        with open("pantheon_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pantheons": []}

# Function to save data to file
def save_data(data):
    with open("pantheon_data.json", "w") as file:
        json.dump(data, file, indent=4)

# Function to display menu
def display_menu():
    print("\nPantheon Manager")
    print("1. List Pantheons")
    print("2. Add Pantheons")
    print("3. Remove Pantheon")
    print("4. Add Gods to Pantheon")
    print("5. Remove God from Pantheon")
    print("6. List Gods in Pantheon")
    print("7. Exit")

# Function to list pantheons
def list_pantheons(data):
    print("\nList of Pantheons:")
    for index, pantheon in enumerate(data["pantheons"], start=1):
        print(f"{index}. {pantheon['name']}")

# Function to add pantheons
def add_pantheons(data):
    pantheon_names = input("\nEnter the names of the new pantheons (comma-separated): ").split(",")
    for pantheon_name in pantheon_names:
        data["pantheons"].append({"name": pantheon_name.strip(), "gods": []})
    save_data(data)
    print(f"\n{', '.join(pantheon_names)} have been added to the list of pantheons.")

# Function to remove a pantheon
def remove_pantheon(data):
    list_pantheons(data)
    pantheon_index = int(input("\nEnter the index of the pantheon to remove: ")) - 1
    pantheon_name = data["pantheons"][pantheon_index]["name"]
    del data["pantheons"][pantheon_index]
    save_data(data)
    print(f"\n'{pantheon_name}' has been removed from the list of pantheons.")

# Function to add gods to a pantheon
def add_gods(data):
    list_pantheons(data)
    pantheon_index = int(input("\nEnter the index of the pantheon to add gods to: ")) - 1
    god_names = input("Enter the names of the new gods (comma-separated): ").split(",")
    for god_name in god_names:
        data["pantheons"][pantheon_index]["gods"].append(god_name.strip())
    save_data(data)
    print(f"\n{', '.join(god_names)} have been added to the selected pantheon.")

# Function to remove a god from a pantheon
def remove_god(data):
    list_pantheons(data)
    pantheon_index = int(input("\nEnter the index of the pantheon to remove a god from: ")) - 1
    pantheon = data["pantheons"][pantheon_index]
    print("\nList of Gods in Selected Pantheon:")
    for index, god in enumerate(pantheon["gods"], start=1):
        print(f"{index}. {god}")
    god_index = int(input("\nEnter the index of the god to remove: ")) - 1
    god_name = pantheon["gods"][god_index]
    del pantheon["gods"][god_index]
    save_data(data)
    print(f"\n'{god_name}' has been removed from the selected pantheon.")

# Function to list gods in a pantheon
def list_gods(data):
    list_pantheons(data)
    pantheon_index = int(input("\nEnter the index of the pantheon to list gods from: ")) - 1
    pantheon = data["pantheons"][pantheon_index]
    print("\nList of Gods in Selected Pantheon:")
    for god in pantheon["gods"]:
        print(f"- {god}")

def main():
    data = load_data()
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            list_pantheons(data)
        elif choice == "2":
            add_pantheons(data)
        elif choice == "3":
            remove_pantheon(data)
        elif choice == "4":
            add_gods(data)
        elif choice == "5":
            remove_god(data)
        elif choice == "6":
            list_gods(data)
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
