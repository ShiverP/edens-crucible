import json

PANTHEON_DATA_FILE = "pantheon_data.json"

# Function to load data from file
def load_data():
    try:
        with open(PANTHEON_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pantheons": []}

# Function to save data to file
def save_data(data):
    with open(PANTHEON_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

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

# Function to list pantheons
def list_pantheons(data):
    print("\nList of Pantheons:")
    for index, pantheon in enumerate(data["pantheons"], start=1):
        print(f"{index}. {pantheon['name']}")

# Main function
def main():
    data = load_data()
    while True:
        print("\nPantheon Builder")
        print("1. List Pantheons")
        print("2. Add Pantheons")
        print("3. Remove Pantheon")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            list_pantheons(data)
        elif choice == "2":
            add_pantheons(data)
        elif choice == "3":
            remove_pantheon(data)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
