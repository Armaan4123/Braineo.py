greet = {"hola","hey","hello","hi","hola neo","hey neo","hello neo","hi neo"}
quizI = {"quiz","quiz me","quiz me neo"}
print ("you can start a quiz by saying 'quiz me neo'")
print ("you can greet neo by saying 'hi'")
I1=str(input("                            hello I am Neo How can I help you?               "))


def greeting():
	print("hello ,I am NEO ... Nice to meet you..!!")

def quiz():
	print("what is the biggest two digit number that is divisible by 2?")
    I2 = str(input("                            "))
    if I2 == '98':
    	print("good !! , correct Answer")
    if I1 in greet :
		greeting()
	elif I2 in quizI :
		quiz()

