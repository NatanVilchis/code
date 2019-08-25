#coding: utf-8
global semilla, a, c, m

semilla=""
temp=""
for letra in semilla:
	temp+=str(ord(letra))
semilla=int(temp)
m=1
a=2
c=3

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
