#coding: utf-8
import os

global semilla, a, c, m

semilla=input("Semilla: ")
temp=""
for letra in semilla:
	temp+=str(ord(letra))
semilla=int(temp)
m=int(eval(input("m: ")))
a=int(eval(input("a: ")))
c=int(eval(input("c: ")))
steps=int(eval(input("steps: ")))
n=int(input("n: "))
OS_choices=["desktop","termux"]
OS=""
while not OS in OS_choices:
	OS=input("desktop|termux: ")

def aleatorio():
	global semilla, a, c,m
	semilla=(a*semilla+c)%m
	return semilla

temp=""
x=0
txt=open(".localkey","w")
for i in range(n):
	z=aleatorio()
	temp_char=chr(steps+int(str(z)[:2]))
	txt.write(temp_char)
	x+=1
txt.close()
if OS=="termux":
	os.system("cat .localkey | termux-clipboard-set")
else:
	os.system("xclip -sel cli < .localkey")
os.remove(".localkey")
