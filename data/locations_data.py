# each location has a list of adjacent locations that must
# be traveled to in order to reach it
LOCATIONS = {
    # police station locations
    "Police Station - Lobby": [
        "Police Station - My Desk",
        "Police Station - Captain's Office",
        "Marketplace - Main Street",
    ],
    "Police Station - My Desk": [
        "Police Station - Lobby",
        "Police Station - Captain's Office",
    ],
    "Police Station - Captain's Office": [
        "Police Station - Lobby",
        "Police Station - My Desk",
    ],

    # bakery locations
    "Bakery - Front Counter": [
        "Bakery - Kitchen",
        "Marketplace - Main Street",
    ],
    "Bakery - Kitchen": ["Bakery - Front Counter", "Bakery - Storage Room"],
    "Bakery - Storage Room": [ "Bakery - Kitchen"],

    # marketplace locations
    "Marketplace - Main Street": [
        "Bakery - Front Counter",
        "Marketplace - Rival Bakery Stall",
        "Marketplace - Loading Area",
        "Police Station - Lobby",
    ],
    "Marketplace - Rival Bakery Stall": [
        "Marketplace - Main Street",
        "Marketplace - Loading Area",
    ],
    "Marketplace - Loading Area": [
        "Marketplace - Main Street",
        "Marketplace - Rival Bakery Stall",
    ],
}
