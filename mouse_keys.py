import pyautogui
from pynput.keyboard import Key, Listener, KeyCode
from time import sleep

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0




x_sens = 20
y_sens = x_sens + 10

mouse_movement_keys = {"i":(0,-y_sens),"k":(0,y_sens),"j":(-x_sens,0),"l":(x_sens,0)}
mouse_click_buttons = {"u":'left',"o":"right"}



def on_press(key):

	for letter,distance in mouse_movement_keys.items():
		if key == KeyCode.from_char(letter):
			pyautogui.move(distance)
			sleep(0/60)

	for letter,button in mouse_click_buttons.items(): 
		if key == KeyCode.from_char(letter):
			pyautogui.mouseDown(button=button)
			sleep(0/60)


def on_release(key):

	for letter,button in mouse_click_buttons.items(): 
		if key == KeyCode.from_char(letter):
			pyautogui.mouseUp(button=button)
			sleep(0/60)

listener = Listener(on_press = on_press ,on_release = on_release)
listener.start()

while True:
	pass
