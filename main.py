from machine import Pin
import time
from time import sleep
from player import Player
from team import Team
from dashboard import Dashboard
from buzzer import Buzzer
from neopixel import NeoPixel

T1P1_BUTTON_PIN = 33
T1P2_BUTTON_PIN = 27
T1P3_BUTTON_PIN = 12
T1P1_LED_PIN = 32
T1P2_LED_PIN = 26
T1P3_LED_PIN = 14

T2P1_BUTTON_PIN = 18
T2P2_BUTTON_PIN = 21
T2P3_BUTTON_PIN = 23
T2P1_LED_PIN = 5
T2P2_LED_PIN = 19
T2P3_LED_PIN = 22

PIXEL_DATA_PIN = 4
PIXEL_LED_COUNT = 16




class Main():
    def __init__(self, teams):
        self.buzzer = Buzzer()
        self.winning_team = None
        self.teams = teams
        #self.game_reset()

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
        
    def start_boot_up(self):
        for team in self.teams:
            team.reset_dashboard()
            for player in team.players:
                player.color_pin.on()
    def end_boot_up(self):
        for team in self.teams:
            for player in team.players:
                player.color_pin.off()
    def game_reset(self):
        print("game_reset")
        for team in self.teams:
            for player in team.players:
                player.color_pin.off()
                #print("light off")
        
        for team in self.teams:
            team.reset_dashboard()
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

def wait_for_start(team1, team2):
    print('clear lights')
    pixels.fill((0,0,0))
    pixels.write()
    time.sleep(0.05)
    pixels.write()
    print('waiting for start')
    while True:
        for team in [team1,team2]:
            for player in team.players:
                if player.button_pin.value():
                    return
def start_lights():
    pixels.fill((0,30,0))
    pixels.write()
    time.sleep(0.05)
    pixels.write()
    time.sleep(1)

print(f'Neopixel on pin {PIXEL_DATA_PIN}.')
pixels = NeoPixel(Pin(PIXEL_DATA_PIN), PIXEL_LED_COUNT)
team1 = Team(1, [x for x in range(int(PIXEL_LED_COUNT/2))], (0,0,30), pixels)
team2 = Team(2, [x for x in range(int(PIXEL_LED_COUNT/2),PIXEL_LED_COUNT)], (30,30,0), pixels)

start_lights()
print('Initializing teams')
team1_config, team2_config = init_config()
register_players_for_team(team1, team1_config)
register_players_for_team(team2, team2_config)
wait_for_start(team1,team2)
game = Main([team1,team2])
game.start_boot_up()
game.buzzer.play_jeopardy_song()
game.register_buttons()
game.end_boot_up()
print('played song')
game.game_reset()
game.game_loop()


