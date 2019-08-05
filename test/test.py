import sys
import os


print(sys.path)
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))
print(sys.path.append(os.path.dirname(os.path.abspath(__file__))))