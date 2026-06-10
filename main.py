from game_state import GameState
from data.locations_data import LOCATIONS

# Create the game state object that tracks player progress.
game_state = GameState()

# Display the title screen once at startup.
print("================================")
print("       LARP SIDE DETECTIVE")
print("================================")
print()
input("Press Enter to begin...")

# Main game loop - continues until the player quits.
while True:
    print("================================")
    print("Current Location:")
    print(game_state.current_location)
    print("================================")
    print()

    print("1. Move")
    print("2. Quit")
    print()

    choice = input("> ")

    # Handle movement between connected locations.
    if choice == "1":

        # Keep the player in the movement menu until they move or cancel.
        while True:

            # Retrieve valid destinations from the current location.
            available_locations = LOCATIONS[game_state.current_location]

            print()
            print("Where would you like to go?")
            print()

            # Dynamically generate the movement menu.
            for index, location in enumerate(available_locations, start=1):
                print(f"{index}. {location}")

            print(f"{len(available_locations) + 1}. Cancel")
            print()

            move_choice = input("> ")

            # Ensure the input can safely be converted to an integer.
            if move_choice.isdigit():
                move_choice = int(move_choice)

                # Move the player to the selected destination.
                if 1 <= move_choice <= len(available_locations):
                    game_state.current_location = available_locations[move_choice - 1]

                    print()
                    print(f"Traveling to {game_state.current_location}...")
                    print()

                    # Exit the movement menu after a successful move.
                    break

                # Return to the main menu without changing location.
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

    elif choice == "2":
        print()
        print("Goodbye.")
        break

    else:
        print()
        print("Invalid choice.")
        print()
