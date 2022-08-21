#coding: utf-8
import os
import platform
import getpass
global semilla, a, c, m

res = input("¿Hidden? (Y/N)?: ").lower()
if res == "y":
  F = getpass.getpass
else:
  F = input 

semilla = F("Semilla: ")
temp = ""
for letra in semilla:
  temp += str(ord(letra))



semilla = int(temp)
m = int(eval(F("m: ")))
a = int(eval(F("a: ")))
c = int(eval(F("c: ")))
steps = int(eval(F("steps: ")))
n = int(F("n: "))

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
  os.system("pbcopy < .localkey")
os.remove(".localkey")

