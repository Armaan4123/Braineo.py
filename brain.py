greetI = {"hola","hey","hello","hi","hola neo","hey neo","hello neo","hi neo"}
quizI = {"quiz","quiz me","quiz me neo"}
singI = {"sing","sing a song"}
I1 = str(input("hello how may I help you? "))

def greet():
	print("hello ,I am NEO ... Nice to meet you..!!")

def sing():
	print("I don't actually have a mouth!!!")

def quiz():
	I2 = str(input("what is the biggest two digit number that is divisible by 2?"))
	if I2 == '98':
		print("good,correct answer!!")
	else :
		print("hmmm!!! try again later")

if I1 in greetI :
	greet()
elif I1 in quizI:
	quiz()
elif I1 in singI:
	sing()
else:
	print ("sometimes I don't understand you!!!")

