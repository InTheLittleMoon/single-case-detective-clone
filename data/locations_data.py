LOCATIONS = {
    "Police Station - Lobby": [
        "Police Station - Front Desk",
        "Police Station - Captain's Office",
        "Bakery - Front Counter",
        "Marketplace - Main Street",
    ],
    "Police Station - Front Desk": [
        "Police Station - Lobby",
        "Police Station - Captain's Office",
    ],
    "Police Station - Captain's Office": [
        "Police Station - Lobby",
        "Police Station - Front Desk",
    ],
    "Bakery - Front Counter": [
        "Bakery - Kitchen",
        "Bakery - Storage Room",
        "Police Station - Lobby",
    ],
    "Bakery - Kitchen": ["Bakery - Front Counter", "Bakery - Storage Room"],
    "Bakery - Storage Room": ["Bakery - Front Counter", "Bakery - Kitchen"],
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
