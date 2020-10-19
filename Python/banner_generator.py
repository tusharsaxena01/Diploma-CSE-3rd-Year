#Custom Ascii Banner using Python

#pip install pyfiglet
'''
Creating this module in order for me to quickly create Fancy banner for my programs
and the syntax to execute is present at the last line
'''
import pyfiglet
from pyfiglet import Figlet
import random

def generate(text):
	approach = random.randint(0,4)
	if approach == 0:
		#Basic Code to print ascii text using pyfiglet
		ascii_text = pyfiglet.figlet_format(text)
		print(ascii_text)
	elif approach == 1:
		#Changing the font to smkeyboard
		font_change = Figlet(font = 'smkeyboard')
		print(font_change.renderText(text))
	elif approach == 2:
		#Changing the font to grafitti
		font_change = Figlet(font='graffiti')
		print(font_change.renderText(text))
	elif approach == 3:
		#Changing the font to zig zag
		font_change = Figlet(font='zig_zag_')
		print(font_change.renderText(text))
	elif approach == 4:
		#Changing the font to wavy
		font_change = Figlet(font='wavy')
		print(font_change.renderText(text))
	elif approach == 5:
		#Changing the font to tubular
		font_change = Figlet(font='tubular')
		print(font_change.renderText(text))
	else:
		pass
'''
Syntax to call this banner generator
Pass 1 argument in str format which would be printed out
'''
#generate("Text")