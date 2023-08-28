from machine import Pin
import time
from player import Player
from team import Team

class Main():
    def __init__(self, teams):
        self.teams = teams
        self.game_reset()
#     r = Pin(2,Pin.OUT)
#     #g = Pin(4,Pin.OUT)
#     b = Pin(16,Pin.OUT)
#     r.off()
#     # g.on()
#     b.off()
#     button1 = Pin(19, Pin.IN, Pin.PULL_DOWN)
#     button2 = Pin(23, Pin.IN, Pin.PULL_DOWN)
#     players = {1:(r,button1), 2:(b,button2)}

    #winner_id = None
    def on_button_press(self,button):
        #player_id = [k for k,v in players.items() if v[1] == button][0]
        for team in self.teams:
            if team.has_button(button):
                self.set_winner(team)
        
    def set_winner(self,team):
        if self.winning_team != None:
            return
        self.winning_team = team
        print(f"Winner is Team {team.team_number}")
        #winner_light()

    def winner_light(self):
        self.winning_team.players[0].color_pin.on()
        #game_reset()
        
    def register_buttons(self):
        for team in self.teams:
            for player in team.players:
                player.button_pin.irq(trigger=Pin.IRQ_RISING, handler=self.on_button_press)
#         button1.irq(trigger=Pin.IRQ_RISING, handler=self.on_button_press)
#         button2.irq(trigger=Pin.IRQ_RISING, handler=self.on_button_press)
        print("Buttons registered")
        
    def game_reset(self):
        for team in self.teams:
            for player in team.players:
                player.color_pin.off()
                #print("light off")
        self.winning_team = None
        
    #self.register_buttons()

    def game_loop(self):
        while True:
            if self.winning_team != None:
                self.winner_light()
                time.sleep(5)
                self.game_reset()

team1 = Team(1)
team2 = Team(2)
player1 = Player(1, Pin(19, Pin.IN, Pin.PULL_DOWN), Pin(2,Pin.OUT))
player2 = Player(2, Pin(23, Pin.IN, Pin.PULL_DOWN), Pin(16,Pin.OUT))
team1.players.append(player1)
team2.players.append(player2)
game = Main([team1,team2])
game.register_buttons()
game.game_loop()
#print(game.teams[1].players[0].number)

