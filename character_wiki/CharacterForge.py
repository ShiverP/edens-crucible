import json

CHARACTER_DATA_FILE = "character_data.json"

# Function to load character data from file
def load_character_data():
    try:
        with open(CHARACTER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"characters": []}

# Function to save character data to file
def save_character_data(data):
    with open(CHARACTER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to create a new character sheet
def create_character():
    print("\nCreating a New Character Sheet")
    character = {}
    character["name"] = input("Enter character name: ")
    character["age"] = input("Enter character age: ")
    character["gender"] = input("Enter character gender: ")
    character["occupation"] = input("Enter character occupation: ")
    character["attributes"] = {}
    character["skills"] = {}
    character["abilities"] = {}
    character["equipment"] = {}
    save_character_data(character)
    print(f"\nCharacter sheet for '{character['name']}' has been created.")

# Function to display character details
def display_character(character):
    print("\nCharacter Sheet:")
    print(f"Name: {character['name']}")
    print(f"Age: {character['age']}")
    print(f"Gender: {character['gender']}")
    print(f"Occupation: {character['occupation']}")
    print("\nAttributes:")
    for attribute, value in character["attributes"].items():
        print(f"- {attribute}: {value}")
    print("\nSkills:")
    for skill, level in character["skills"].items():
        print(f"- {skill}: {level}")
    print("\nAbilities:")
    for ability, description in character["abilities"].items():
        print(f"- {ability}: {description}")
    print("\nEquipment:")
    for item, description in character["equipment"].items():
        print(f"- {item}: {description}")

# Main function
def main():
    data = load_character_data()
    while True:
        print("\nCharacter Forge")
        print("1. Create New Character Sheet")
        print("2. View Character Sheet")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            create_character()
        elif choice == "2":
            if not data["characters"]:
                print("\nNo character sheets available.")
            else:
                print("\nAvailable Character Sheets:")
                for index, character in enumerate(data["characters"], start=1):
                    print(f"{index}. {character['name']}")
                character_index = int(input("\nEnter the index of the character to view: ")) - 1
                display_character(data["characters"][character_index])
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
