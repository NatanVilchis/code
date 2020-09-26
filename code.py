#coding: utf-8

import os
import platform
import getpass
global semilla, a, c, m


semilla = getpass.getpass("Semilla: ")
temp = ""
for letra in semilla:
  temp += str(ord(letra))



semilla = int(temp)
m = int(eval(getpass.getpass("m: ")))
a = int(eval(getpass.getpass("a: ")))
c = int(eval(getpass.getpass("c: ")))
steps = int(eval(getpass.getpass("steps: ")))
n = int(getpass.getpass("n: "))

def aleatorio():
  global semilla, a, c,m
  semilla = (a*semilla+c)%m
  return semilla

temp = ""
x = 0
txt = open(".localkey","w")
for i in range(n):
  z = aleatorio()
  temp_char = chr(steps+int(str(z)[:2]))
  txt.write(temp_char)
  temp += temp_char 
  x += 1
txt.close()



if platform.uname().system == "Linux":
  if platform.uname().machine == "x86_64":
    os.system("xclip -sel cli < .localkey")
  elif platform.uname().machine == "aarch64":
    os.system("cat .localkey | termux-clipboard-set")
  else:
    print("Not supported",platform.uname())
elif platform.uname().system == "Windows":
  os.system("echo " + temp + "| clip")
else:
  print("Not supported",platform.uname())
os.remove(".localkey")
