# For loop is used for sequential traversal. For traversing list.

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

for num in tup:
    print(num)              

character = "ham sab ka Pakistan"

for char in character:
    if(char == "P"):
        print("o found")
        break
    print(char)
else:
    print("end")                

# WAP to print the elements of the following 

set = [1, 4, 9, 16, 25, 49, 64,81, 100]

for elements in set:
    print(elements) 
else:
    print("end of loop") 

# WAP to search num x in the following tuple using Loop 

set = (1, 4, 9, 16, 25, 49, 64,81, 100)

x = int(input("type the num : "))

i = 0

for ele in set:
    if(ele == x):
        print("Found at : ", i)

    i +=  1
   
# range
# Range function returns a sequence of numbers, starting from the 0 by default and increments 
# increments by 1 and stops before a specified number.

range(start?, stop, step?)
print(range(5))

seq = range(10)

for i in seq:
    print(i)              

asm = range(13)

for i in asm:
    print(i)     


for i in range(2, 10): #range (start, stop)
    print(i)



WAP to print the numbers from 1 to 100

for i in range (1, 101):
    print(i)              

# WAP to print nums from 100 t0 1              

for i in range (101, 0, -1):
    print(i)


print the multiplication num of N


num = int(input("type the num : "))

i = 0

for i in range(1, 11):
    print(num * i)

    i += 1    
        
factorial of n number

num = 8

fact = 1

i = 1

while i<= 8:
    fact *= i

    i += 1
print(" Fcat of num : ", fact)    



num = 8

fact = 1

i = 1

while i <= 8:
    fact *= i

    i += 1
print("fact : ", fact)    


num = int(input("type num : "))

fact = 1

i = 1

while i <=num:
    fact *= i

    i += 1
print("fact of num : ", fact)    

