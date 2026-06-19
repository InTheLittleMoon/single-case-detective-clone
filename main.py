from game_state import GameState
from data.locations_data import LOCATIONS


# Handles player movement between connected locations
def handle_movement(game_state):

    while True:
        available_locations = LOCATIONS[game_state.current_location]

        # Story gate: before investigation starts, restrict certain areas
        if "talked_to_captain" not in game_state.flags:
            blocked_locations = {
                "Bakery - Kitchen",
                "Bakery - Storage",
                "Marketplace - Loading Area",
            }

            available_locations = [
                loc for loc in available_locations if loc not in blocked_locations
            ]
            
            
        print()
        print("Where would you like to go?")
        print()

        # Display all connected locations
        for index, location in enumerate(available_locations, start=1):
            print(f"{index}. {location}")

        print(f"{len(available_locations) + 1}. Cancel")
        print()

        move_choice = input("> ")

        # Validate movement input
        if move_choice.isdigit():
            move_choice = int(move_choice)

            # Travel to selected location
            if 1 <= move_choice <= len(available_locations):
                game_state.current_location = available_locations[move_choice - 1]

                print()
                print(f"Traveling to {game_state.current_location}...")
                print()

                break

            # Return to previous menu
            elif move_choice == len(available_locations) + 1:
                print()
                print("Travel cancelled.")
                print()

                break

            else:
                print()
                print("Invalid destination.")
                print()

        else:
            print()
            print("Please enter a number.")
            print()


# Displays actions available at the current location
def show_location_menu(game_state):

    location = game_state.current_location

    print()

    if location == "Police Station - Lobby":
        print("1. Move")
        print("2. Quit")

    elif location == "Bakery - Front Counter":
        print("1. Look Around")
        print("2. Move")
        print("3. Quit")

    elif location == "Marketplace - Main Street":
        print("1. Look Around")
        print("2. Move")
        print("3. Quit")

    # Fallback menu for locations not yet implemented
    else:
        print("1. Move")
        print("2. Quit")

    print()


# Create a new game state object
game_state = GameState()


# Title screen
print("================================")
print("       LARP SIDE DETECTIVE")
print("================================")
print()
input("Press Enter to begin...")


# Main game loop
while True:

    # Current location header
    print("================================")
    print("Current Location:")
    print(game_state.current_location)
    print("================================")
    print()

    show_location_menu(game_state)

    choice = input("> ")

    location = game_state.current_location

    # Police Station Lobby actions
    if location == "Police Station - Lobby":

        if choice == "1":
            handle_movement(game_state)

        elif choice == "2":
            print()
            print("Goodbye.")
            break

        else:
            print()
            print("Invalid choice.")
            print()

    # Bakery actions
    elif location == "Bakery - Front Counter":

        if choice == "1":
            print()
            print("The smell of fresh bread fills the air.")
            print("Maybe I'll grab a dozen before heading back to the office.")
            print()

        elif choice == "2":
            handle_movement(game_state)

        elif choice == "3":
            print()
            print("Goodbye.")
            break

        else:
            print()
            print("Invalid choice.")
            print()

    # Marketplace actions
    elif location == "Marketplace - Main Street":

        if choice == "1":
            print()
            print("What a nice day.")
            print("Maybe I'll come back here with my lady later.")
            print()

        elif choice == "2":
            handle_movement(game_state)

        elif choice == "3":
            print()
            print("Goodbye.")
            break

        else:
            print()
            print("Invalid choice.")
            print()

    # Fallback location handling
    else:

        if choice == "1":
            handle_movement(game_state)

        elif choice == "2":
            print()
            print("Goodbye.")
            break

        else:
            print()
            print("Invalid choice.")
            print()
