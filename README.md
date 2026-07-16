# LARP SIDE DETECTIVE

LARP SIDE DETECTIVE is a terminal-based detective game written in Python and inspired by games such as *The Darkside Detective*. Players investigate the theft of a legendary 15-year-old sourdough starter, "Old Crusty," by gathering clues, interacting with NPCs, and progressing through a connected series of locations.

The project was built as a small, story-driven portfolio piece focused on modular code structure, state management, and simple investigation mechanics.

## Features

* Terminal-based detective adventure.
* Dialogue-driven investigation and clue discovery.
* Location-based movement system.
* Story progression through NPC interactions and environmental clues.
* Modular location action handlers.
* Dynamic dialogue based on investigation progress.

## Game Flow

```text
Police Station
    ↓
Captain assigns the case.
    ↓
Bakery Investigation
    ↓
Kitchen & Storage Room clues.
    ↓
Marketplace Loading Area.
    ↓
Rival Baker Stall.
    ↓
Return to the Captain.
    ↓
Case Closed.
```

## Mechanics

### Movement System

Players can only travel between connected locations. Certain areas remain inaccessible until the appropriate story events have occurred.

Examples:

* Bakery back rooms unlock after speaking with the Baker.
* Marketplace Loading Area unlocks after discovering the Bakery clue.
* Rival Baker Stall unlocks after investigating the Loading Area.

### Investigation System

The investigation progresses through dialogue, environmental observations, and discovered clues. Player actions update the game state and unlock new interactions as the case develops.

## Technologies Used

* Python 3
* Terminal / Command Line Interface (CLI)

No external libraries or frameworks are required.

## Running the Game

From the project directory:

```bash
python main.py
```

Follow the on-screen prompts to begin the investigation.
