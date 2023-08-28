from machine import Pin
import time
r = Pin(2,Pin.OUT)
#g = Pin(4,Pin.OUT)
b = Pin(16,Pin.OUT)
r.off()
# g.on()
b.off()
button1 = Pin(19, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(23, Pin.IN, Pin.PULL_DOWN)
players = {1:(r,button1), 2:(b,button2)}

winner_id = None
def on_button_press(button):
    player_id = [k for k,v in players.items() if v[1] == button][0]
    determine_winner(player_id)
    
def determine_winner(player_id):
    global winner_id
    if winner_id != None:
        return
    winner_id = player_id
    print(f"Winner is Player {winner_id}")
    #winner_light()

def winner_light():
    players[winner_id][0].on()
    #game_reset()
    
def register_buttons():
    button1.irq(trigger=Pin.IRQ_RISING, handler=on_button_press)
    button2.irq(trigger=Pin.IRQ_RISING, handler=on_button_press)
    print("Buttons registered")
    
def game_reset():
    global winner_id
    players[winner_id][0].off()
    winner_id = None
    
register_buttons()

def game_loop():
    while True:
        if winner_id != None:
            winner_light()
            time.sleep(5)
            game_reset()
game_loop()