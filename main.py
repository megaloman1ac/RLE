import time
#from modules import encode
from modules.encode import *
from modules.decode import *

print("Hello, World!")

#encode.encode("s")
inp = input("Enter your word: ")
print(encode(inp))
print(decode(encode(inp)))
