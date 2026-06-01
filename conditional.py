light = "green"

if(light == "red"):
    print("stop")
elif(light == "blue"):
    print("ready")
elif(light == "green"):
    print("go")    
else:
    print("broken") 

light = "red"

if (light == "blue"):
    print("ready")
elif(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
else:
    print("broken") 

marks = int(input("marks : "))

if (marks >= 90):
    print("Grade A")
elif (marks >= 80 and marks <= 90):
    print("Grade B")
elif (marks >= 70 and marks <= 80):
    print("Grade C")
else:
    print("fail")                          

# WAP to check the no entered by the user is even or odd

num = int(input("enter number : "))

if (num % 2 == 0):
    print("Even")
else:
    print("odd")    

# or
num = int(input("enter number : "))


if (num % 2 == 0):
    print("Even")
else:
    print("Odd")                  

# WAP to find the greates of teh 3 number provided by user?

a =int(input("enter 1st num : "))
b = int(input("enter 2nd number : "))
c = int(input("enter 2nd number : "))

if(a > b and a > c):
    print("a is greater")
elif(b > c):
    print("b is greater")
else: 
    print("C is greater")

# WAP to check the num is multiple of  7 or not?
num = int(input("Enter Number : "))

if(num % 5 == 0):
    print("multiple of 5")
else:
    print("Not")            


   
