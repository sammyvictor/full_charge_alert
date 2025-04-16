import os
import time
import psutil
import pygame

def play_alert_sound():
    pygame.mixer.init()
    sound_path = os.path.join(os.path.dirname(__file__), "charge_complete.mp3")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def check_battery():
    battery = psutil.sensors_battery()
    if battery and battery.percent >= 99 and battery.power_plugged:
        # print("Battery is full. Unplug the charger.")
        play_alert_sound()

while True:
    check_battery()
    time.sleep(30) 
    