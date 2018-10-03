#simple calculator
i=int(input("enter the value of i"))
j=int(input("enter the value of j"))
o=input("what do u want to calculte:[+],[-],[*],[/]?")
def add():
	return i+j
def sub():
	return i-j
def mul():
	return i*j
def div():
	return i/j
if(o=='+'):
	print("addition = ",add())
elif(o=='-'):
	print("substraction = ",sub())
elif(o=='*'):
	print("multiplication = ",mul())
elif(o=='/'):
	print("division = ",div())
