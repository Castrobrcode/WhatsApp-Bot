#Bibliotecas 
import pywhatkit
import keyboard
import time
from datetime import datetime

#Contatos

contatos = ['+5521964577055']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'Ola, Mundo', datetime.now().hour, datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('crtl + w')