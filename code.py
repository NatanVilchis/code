#coding: utf-8

import os
import platform
global semilla, a, c, m


semilla = input("Semilla: ")
temp = ""
for letra in semilla:
  temp += str(ord(letra))



semilla = int(temp)
m = int(eval(input("m: ")))
a = int(eval(input("a: ")))
c = int(eval(input("c: ")))
steps = int(eval(input("steps: ")))
n = int(input("n: "))

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
elif platform.uname().system == "Windows":
  os.system("echo " + temp + "| clip")
os.remove(".localkey")
