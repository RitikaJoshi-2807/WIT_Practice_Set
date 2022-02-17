name=input ("Enter your name : ")
print( "Hello, "+name.capitalize() +". Welcome to the calculator application!.")
number=int(input("Choose the number of arithmetic operations below :\n1. Adiition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus operation\n"))
a=int(input("Enter the value of a:"))
b=int(input ("Enter the value of b:"))
if(number==1):
    print(a+b)
elif(number==2):
    print(a-b)
elif(number==3):
    print(a*b)
elif(number==4):
    print(a/b)
elif(number==5):
    print(a%b)
else:
    print("Choose valid operation")
