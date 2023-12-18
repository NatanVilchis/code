# coding: utf-8
import os
import platform
import getpass
import random 

res = input("¿Hidden? (Y/N)?: ").lower()
if res == "y":
  F = getpass.getpass
else:
  F = input 

seed = F("Semilla: ")
n = int(F("n: "))

random.seed(seed)
tmp = "".join([chr(i) for i in random.choices(range(32,11001),k=n)])

txt = open(".localkey","w")
txt.write(tmp)
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
