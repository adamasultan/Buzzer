class Team:
    def __init__(self, team_number):
        self.players = []
        self.team_number = team_number
        
    def has_button(self,button):
        for player in self.players:
            if button == player.button_pin:
                return True
    def get_player(self, button):
        for player in self.players:
            if button == player.button_pin:
                return player