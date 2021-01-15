#this code sets up the lcd and prints a simple message out onto it
#gathered some inspiration and learned from:
#https://www.mbtechworks.com/projects/drive-an-lcd-16x2-display-with-raspberry-pi.html

import RPi.GPIO as GPIO
import time 

#setup the lcd with the correct pins
LCD_RS = 26
LCD_E = 19
LCD_D4 =  13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
LED_ON = 15
LCD_CHR = True
LCD_CMD = False
LCD_CHARS = 16 #my display is 16x2 = 16 chars in 2 lines
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0


def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_D4, GPIO.OUT)
	GPIO.setup(LCD_D5, GPIO.OUT)
	GPIO.setup(LCD_D6, GPIO.OUT)
	GPIO.setup(LCD_D7, GPIO.OUT)
	
	lcd_init()

#the text below is what actual print out onto the screen! "line 1" should be on top, and "line 2" should be on the bottom
	while True:
		lcd_text("line 1",LCD_LINE_1)
		lcd_text("line 2",LCD_LINE_2)
		
def lcd_init():
	lcd_write(0x33, LCD_CMD)
	lcd_write(0x32, LCD_CMD)
	lcd_write(0x06, LCD_CMD)
	lcd_write(0x0C, LCD_CMD)
	lcd_write(0x28, LCD_CMD)
	lcd_write(0x01, LCD_CMD)
	time.sleep(0.0005)
	
def lcd_write(bits, mode):
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	
	if bits&0x10==0x10:
		GPIO.output(LCD_D4, True)
	if bits&0x20==0x20:
		GPIO.output(LCD_D5, True)
	if bits&0x40==0x40:
		GPIO.output(LCD_D6, True)
	if bits&0x80==0x80:
		GPIO.output(LCD_D7, True)
		
	lcd_toggle_enable()
	
def lcd_toggle_enable():
	time.sleep(0.0005)
	GPIO.output(LCD_E, True)
	time.sleep(0.0005)
	GPIO.output(LCD_E, False)
	time.sleep(0.0005)
	
def lcd_text(message, line):
	message = message.ljust(LCD_CHARS," ")
	lcd_write(line, LCD_CMD)
	
	for i in range(LCD_CHARS)
		lcd_write(ord(message[i]),LCD_CHR)
		
try:
	main()
except KeyboardInterupt:
	pass
