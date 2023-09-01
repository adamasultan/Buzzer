from machine import Pin
import time
from time import sleep
from player import Player
from team import Team
from dashboard import Dashboard
from buzzer import Buzzer

T1P1_BUTTON_PIN = 13 #works
T1P2_BUTTON_PIN = 14 #works
T1P3_BUTTON_PIN = 33 #works 
T1P1_LED_PIN = 27 #works
T1P2_LED_PIN = 26 #works
T1P3_LED_PIN = 25 #works

T2P1_BUTTON_PIN = 21 #works
T2P2_BUTTON_PIN = 23 #works
T2P3_BUTTON_PIN = 5 #works
T2P1_LED_PIN = 19 #works
T2P2_LED_PIN = 22 #works
T2P3_LED_PIN = 18 #works



class Main():
    def __init__(self, teams):
        self.buzzer = Buzzer()
        self.winning_team = None
        self.teams = teams
        self.game_reset()
        self.buzzer = Buzzer()

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
        print("Starting game loop")
        while True:
            #print('.', end=" ")
            #sleep(0.1)
            if self.winning_team != None:
                print('')
                self.winner_light()
                self.game_reset()

def register_players_for_team(team, team_config):
    for player_config in team_config:
        register_player(team, player_config[0], player_config[1], player_config[2])


def register_player(team, player_number, button_pin, led_pin):
        player = Player(player_number, Pin(button_pin, Pin.IN, Pin.PULL_DOWN), Pin(led_pin,Pin.OUT))
        team.players.append(player)
        print(f'Player {player_number} on team {team.team_number}: Button: {button_pin}, LED: {led_pin}')    

def init_config():
    team1_config = []
    team1_config.append([1, T1P1_BUTTON_PIN,T1P1_LED_PIN])
    team1_config.append([2, T1P2_BUTTON_PIN,T1P2_LED_PIN])
    team1_config.append([3, T1P3_BUTTON_PIN,T1P3_LED_PIN])  
    print(f'Configured {len(team1_config)} players for team 1')

    team2_config = []
    team2_config.append([1, T2P1_BUTTON_PIN,T2P1_LED_PIN])
    team2_config.append([2, T2P2_BUTTON_PIN,T2P2_LED_PIN])
    team2_config.append([3, T2P3_BUTTON_PIN,T2P3_LED_PIN])
    print(f'Configured {len(team2_config)} players for team 2')

    return team1_config, team2_config

team1 = Team(1, [x for x in range(8)], (255,0,0))
team2 = Team(2, [x for x in range(8,16)], (0,0,255))

print('Initializing teams')
team1_config, team2_config = init_config()
register_players_for_team(team1, team1_config)
register_players_for_team(team2, team2_config)


game = Main([team1,team2])
game.register_buttons()
game.game_loop()
#print(game.teams[1].players[0].number)

