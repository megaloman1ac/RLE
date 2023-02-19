from modules.encode import *
from modules.decode import *

while(True):
	print("Enter your word: ", end = "")
	
	inp = input()
	
	if inp == "exit" or inp == "Exit":
		break
	else:
		print(encode(inp))
		print(decode(encode(inp)))
