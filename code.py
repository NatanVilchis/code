#coding: utf-8
import sys
global semilla, a, c, m

semilla=input("Semilla: ")
temp=""
for letra in semilla:
	temp+=str(ord(letra))
semilla=int(temp)
m=int(eval(input("m: ")))
a=int(eval(input("a: ")))
c=int(eval(input("c: ")))

def aleatorio():
	global semilla, a, c,m
	semilla=(a*semilla+c)%m
	return semilla

temp=""
x=0
txt=open(".localkey","w")
for i in range(25):
	z=aleatorio()
	temp_char=chr(int(str(z)[:2]))
	txt.write(temp_char)
	x+=1
txt.close()
