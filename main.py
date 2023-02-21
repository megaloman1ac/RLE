from modules.encode import *
from modules.decode import *
from modules.console import *
import os

while(True):
	os.system('clear')
	inp = input("Enter your word: ")
	
	if inp == "exit" or inp == "Exit":
		break
	else:
		write(encode(inp), decode(encode(inp)))
	input()
