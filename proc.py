import os
from subprocess import Popen,PIPE
from shlex import split
names = open('names').read()
names.split(" ")
print(names)
result = []
p1 = Popen(split("ls"),stdout=PIPE)
p2 = Popen(split("cat"),  stdin=p1.stdout)
print(p2)

    
