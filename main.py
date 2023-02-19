from modules.encode import *
from modules.decode import *

print("Hello, World!")

inp = input("Enter your word: ")
print(encode(inp))
print(decode(encode(inp)))
