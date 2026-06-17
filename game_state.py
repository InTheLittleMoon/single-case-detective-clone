class GameState:
    def __init__(self):
        # Player starts in the police station lobby.
        self.current_location = "Police Station - Lobby"

        #  Evidence collected during the investigation.
        self.inventory = []

        # Story progression and conversations.
        self.flags = set()