a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print(a[0]+'|' +a[1]+'|' +a[2])
	print("------")
	print(a[3]+'|'+ a[4]+'|' +a[5])
	print("------")
	print(a[6]+'|'+ a[7]+'|' +a[8])	
player1turn=True
for i in range(9):
	printboard()



#player one plays
	if player1turn:
		p=input("player 1 ,choose your place:")
		if p in a:
			a[int(p)-1]='X'
			player1turn=not player1turn
#player two plays
	else:
		p=input("player 2 ,choose your place:")
		if p in a:
			a[int(p)-1]='O'
			player1turn=not player1turn
#checking wining combination
a1=a[0,1,2]
a2=a[3,4,5]
a3=a[6,7,8]
a4=a[0,3,6]
a5=a[1,4,7]
a6=a[2,5,8]
a7=a[0,4,8]
a8=a[2,4,6]
if(a1==X or a2==X or a3==X or a4==X or a5==X or a6==X or a7==X or a8==X):
	print("player 1 wins")
else(a1==0 or a2==0 or a3==0 or a4==0 or a5==0 or a6==0 or a7=0 or a8==0):
	print("player 2 wins")
	exit()





