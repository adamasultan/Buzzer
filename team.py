from dashboard import Dashboard

class Team:
    def __init__(self, team_number, leds, color):
        self.players = []
        self.team_number = team_number
        self.__dashboard = Dashboard(leds, color)
        
    def has_button(self,button):
        for player in self.players:
            if button == player.button_pin:
                return True
    def get_player(self, button):
        for player in self.players:
            if button == player.button_pin:
                return player
    
    def display_win(self):
        self.__dashboard.win()