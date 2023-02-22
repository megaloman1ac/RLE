from time import sleep
from os import system
import re

def scan():
	inp = input("I >> ")
	if inp == "":
		print("A >> There is no word !")
		sleep(1)
		print("\nPress any key to continue ...")
		return "nope"
	elif re.match(r'\s', inp):
		print("A >> There is only spaces !")
		sleep(1)
		print("\nPress any key to continue ...")
		return "nope"
	elif inp == "exit" or inp == "Exit":
		return inp
		
	return inp
		

def write(encoded, decoded):
	sleep(1)
	system('clear')
	print("E >> Encoded string: " + encoded, end='\n')
	sleep(1)
	print("D >> Decoded string: " + decoded, end='\n')
	sleep(1)
	print("\nPress any key to continue ...")
