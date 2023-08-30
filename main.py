from machine import Pin
import time
from player import Player
from team import Team
from dashboard import Dashboard

T1P1_BUTTON_PIN = 13
T1P2_BUTTON_PIN = 12
T1P3_BUTTON_PIN = 14
T1P1_LED_PIN = 26
T1P2_LED_PIN = 25
T1P3_LED_PIN = 33

T2P1_BUTTON_PIN = 5
T2P2_BUTTON_PIN = 18
T3P3_BUTTON_PIN = 19
T2P1_LED_PIN = 15
T2P2_LED_PIN = 2
T2P3_LED_PIN = 4

class Main():
    def __init__(self, teams):
        self.winning_team = None
        self.teams = teams
        self.game_reset()

    def on_button_press(self,button):
        for team in self.teams:
            if team.has_button(button):
                #print(team.get_player(button).number)
                self.set_winner(team.get_player(button),team)
        
    def set_winner(self,player,team):
        if self.winning_team != None:
            return
        self.winning_team = team
        self.winning_player = player
        print(f"Winner is Team {team.team_number}: player:{player.number}")

    def winner_light(self):
        self.winning_player.color_pin.on()
        self.winning_team.display_win()
        print("winner_light")
        
    def register_buttons(self):
        for team in self.teams:
            for player in team.players:
                player.button_pin.irq(trigger=Pin.IRQ_RISING, handler=self.on_button_press)
        print("Buttons registered")
        
    def game_reset(self):
        print("game_reset")
        for team in self.teams:
            for player in team.players:
                player.color_pin.off()
                #print("light off")
        if self.winning_team != None:
            self.winning_team.reset_dashboard()
        self.winning_team = None
        self.winning_player = None

    def game_loop(self):
        print("here")
        while True:
            if self.winning_team != None:
                self.winner_light()
                self.game_reset()



team1 = Team(1, [x for x in range(8)], (255,0,0))
team2 = Team(2, [x for x in range(8,16)], (0,0,255))
player1 = Player(1, Pin(T1P1_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN), Pin(T1P1_LED_PIN,Pin.OUT))

player2 = Player(2, Pin(T2P1_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN), Pin(T2P1_LED_PIN,Pin.OUT))
player3 = Player(3, Pin(T2P2_BUTTON_PIN, Pin.IN, Pin.PULL_DOWN), Pin(T2P2_LED_PIN,Pin.OUT))

team1.players.append(player1)
team2.players.append(player2)
team2.players.append(player3)
game = Main([team1,team2])

game.register_buttons()
game.game_loop()
#print(game.teams[1].players[0].number)

