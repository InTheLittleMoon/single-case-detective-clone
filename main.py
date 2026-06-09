from game_state import GameState
from data.locations_data import LOCATIONS

game_state = GameState()

print("================================")
print("       LARP SIDE DETECTIVE")
print("================================")
print()
input("Press Enter to begin...")

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

    if choice == "1":
        print("Movement coming next.")

    elif choice == "2":
        print()
        print("Goodbye.")
        break

    else:
        print()
        print("Invalid choice.")
        print()
