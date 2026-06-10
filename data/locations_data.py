# each location has a list of adjacent locations that must 
# be traveled to in order to reach it
LOCATIONS = {
    "Police Station - Lobby": [
        "Police Station - My Desk",
        "Police Station - Captain's Office",
        "Bakery - My Counter",
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
    "Bakery - My Counter": [
        "Bakery - Kitchen",
        "Bakery - Storage Room",
        "Police Station - Lobby",
    ],
    "Bakery - Kitchen": ["Bakery - My Counter", "Bakery - Storage Room"],
    "Bakery - Storage Room": ["Bakery - My Counter", "Bakery - Kitchen"],
    "Marketplace - Main Street": [
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
