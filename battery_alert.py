import psutil
import time
import pygame

def play_alert_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("charge_complete.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def check_battery():
    battery = psutil.sensors_battery()
    if battery and battery.percent == 100 and battery.power_plugged:
        # print("Battery is full. Unplug the charger.")
        play_alert_sound()

while True:    
    check_battery()
    time.sleep(60) 