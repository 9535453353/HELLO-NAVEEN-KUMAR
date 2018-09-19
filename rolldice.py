import random

while True:
	x=input("enter 'r' to roll a dice and 'q' to quit the dice")
	if(x=='r'):
		print(random.randint(1,6))
	elif(x=='q'):
		print("bye")
		break
	else:
	    print("give either 'r' or 'q' ")

	
   



