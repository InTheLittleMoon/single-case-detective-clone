from game_state import GameState
from data.locations_data import LOCATIONS


# Handles player movement between connected locations
def handle_movement(game_state):

    while True:
        available_locations = LOCATIONS[game_state.current_location]

        # Story gates: lock investigation areas until the proper story events occur
        blocked_locations = set()

        # Back bakery areas stay locked until you've spoken with the Baker
        if "talked_to_baker" not in game_state.flags:
            blocked_locations.update(
                {
                    "Bakery - Kitchen",
                    "Bakery - Storage Room",
                    "Marketplace - Loading Area",
                }
            )

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


# confirm_quit() prompts the player to confirm quitting the game
def confirm_quit():
    while True:
        answer = (
            input("Are you sure you'd like to quit the game? (y/n) ").strip().lower()
        )
        if answer in ("y", "yes"):
            print()
            print("Goodbye.")
            return True
        if answer in ("n", "no"):
            print()
            print("Quit cancelled.")
            print()
            return False
        print()
        print("Please enter 'y' or 'n'.")
        print()


# DEBUG: Display all active game flags
# Mainly for testing, will remove once complete project is finished
def debug_flags(game_state):
    print()
    print(f"[DEBUG] Current Flags: {sorted(game_state.flags)}")
    print()


# location handlers below
# Handles all actions in the police station locations
def police_station_actions(game_state):

    if game_state.current_location == "Police Station - Lobby":
        print()
        print("1. Talk to Janice")
        print("2. Move")
        print("3. Quit")
        print()

        choice = input("> ")

        if choice == "1":
            print()

            if "talked_to_captain" in game_state.flags:
                print("Janice:")
                print('"Have a good day!"')
            else:
                print("Janice:")
                print('"Morning, detective."')
                print('"The Captain wants to see you."')

            print()
            return False

        elif choice == "2":
            handle_movement(game_state)
            return False

        elif choice == "3":
            return confirm_quit()

        else:
            print()
            print("Invalid choice.")
            print()
            return False

    elif game_state.current_location == "Police Station - Captain's Office":

        print()
        print("1. Talk to Captain")
        print("2. Move")
        print("3. Quit")
        print()

        choice = input("> ")

        if choice == "1":

            print()

            if "talked_to_captain" in game_state.flags:
                print("Captain:")
                print('"The bakery won\'t solve itself."')

            else:
                print("Captain:")
                print('"Morning, detective."')
                print('"The bakery owner reported something stolen overnight."')
                print('"Head over there and see what you can find."')
                print()
                print("Detective:")
                print('"On it, Capt."')

                game_state.flags.add("talked_to_captain")

                ## DEBUG: Display all active game flags, REMOVE ME LATER
                debug_flags(game_state)

            print()
            return False

        elif choice == "2":
            handle_movement(game_state)
            return False

        elif choice == "3":
            return confirm_quit()

        else:
            print()
            print("Invalid choice.")
            print()
            return False

    elif game_state.current_location == "Police Station - My Desk":

        print()
        print("1. Look Around")
        print("2. Move")
        print("3. Quit")
        print()

        choice = input("> ")

        if choice == "1":
            print()
            print("My desk is exactly how I left it.")
            print("Mostly organized... depending on who you ask.")
            print()

            return False

        elif choice == "2":
            handle_movement(game_state)
            return False

        elif choice == "3":
            return confirm_quit()

        else:
            print()
            print("Invalid choice.")
            print()
            return False


# Handles all actions in the Bakery
def bakery_actions(game_state):

    print()
    print("1. Talk to Baker")
    print("2. Talk to Assistant")
    print("3. Move")
    print("4. Quit")
    print()

    choice = input("> ")

    # Baker interaction
    if choice == "1":

        print()

        # Player has not received the case yet
        if "talked_to_captain" not in game_state.flags:
            print("Baker:")
            print('"Welcome in! Let me know if you need anything."')

        # First time discussing the investigation
        elif "talked_to_baker" not in game_state.flags:
            print("Baker:")
            print('"Detective, thank goodness you\'re here."')
            print('"Something was stolen overnight."')
            print("\"I've searched everywhere, but I can't figure out what happened.\"")
            print('"Maybe my assistant noticed something I didn\'t."')

            game_state.flags.add("talked_to_baker")
            debug_flags(game_state)

        # Repeat dialogue after already questioned
        else:
            print("Baker:")
            print('"I hope you find out what happened."')

        print()
        return False

    # Assistant interaction
    elif choice == "2":

        print()

        # No case exists yet
        if "talked_to_captain" not in game_state.flags:
            print("Assistant:")
            print('"Welcome! Let me know if you need anything."')

        # Player knows about case but has not spoken to Baker
        elif "talked_to_baker" not in game_state.flags:
            print("Assistant:")
            print('"Sorry, detective."')
            print('"You should probably speak with the boss first."')

        # First assistant investigation dialogue
        elif "talked_to_assistant" not in game_state.flags:
            print("Assistant:")
            print('"I still can\'t believe this happened."')
            print('"The storage room was definitely locked."')
            print('"I put a piece of stale baguette there..."')
            print('"It could\'ve never been done!"')

            game_state.flags.add("talked_to_assistant")
            debug_flags(game_state)

        # Repeat dialogue
        else:
            print("Assistant:")
            print('"The storage room was definitely locked."')

        print()
        return False

    elif choice == "3":
        handle_movement(game_state)
        return False

    elif choice == "4":
        return confirm_quit()

    else:
        print()
        print("Invalid choice.")
        print()
        return False


# Handles all actions in the Marketplace
def marketplace_actions(game_state):

    print()
    print("1. Look Around")
    print("2. Move")
    print("3. Quit")
    print()

    choice = input("> ")

    if choice == "1":
        print()
        print("What a nice day.")
        print("Maybe I'll come back here with my lady later.")
        print()

        return False

    elif choice == "2":
        handle_movement(game_state)
        return False

    elif choice == "3":
        return confirm_quit()

    else:
        print()
        print("Invalid choice.")
        print()
        return False


def get_location_handler(location):
    if location in {
        "Police Station - Lobby",
        "Police Station - My Desk",
        "Police Station - Captain's Office",
    }:
        return police_station_actions
    if location in {
        "Bakery - Front Counter",
        "Bakery - Kitchen",
        "Bakery - Storage Room",
    }:
        return bakery_actions
    if location in {
        "Marketplace - Main Street",
        "Marketplace - Rival Bakery Stall",
        "Marketplace - Loading Area",
    }:
        return marketplace_actions
    return None


# Main game loop
def main():
    game_state = GameState()

    # Title screen
    print("================================")
    print("      LARP SIDE DETECTIVE")
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

        location = game_state.current_location
        handler = get_location_handler(location)

        if handler is None:
            print("This location has no actions implemented yet.")
            print()
            break

        if handler(game_state):
            break


if __name__ == "__main__":
    main()
