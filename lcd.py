import lcddriver
import time

lcd = lcddriver.lcd()
time.sleep(3)
lcd.Print("_   Emad    _",1)
lcd.Print("Welcome to Pi", 2 )
time.sleep(1)
lcd.Clear()
lcd.Print("_ EjElectro  _",1)
lcd.Print("Welcome to RPi", 2 )
