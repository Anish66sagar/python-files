#program to get random number
import random
while True:
	a=input("enter r to roll dice or q to quit")
	if(a=="r"):
		print(random.randint(1,6))
	else:
         print("bye")
         exit()
     
       
	
