from modules.encode import *
from modules.decode import *
from modules.console import *
from os import system

while(True):
	system('clear')
	inp = scan();
	
	if inp == "exit" or inp == "Exit":
		break
	elif inp != "nope":
		write(encode(inp), decode(encode(inp)))
	input()
