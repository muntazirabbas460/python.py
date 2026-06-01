# Block of Statements that perform the specific function

def cal_sum(a, b):
    sum = a + b
    print(sum)
    return(sum)

cal_sum(5, 30)              
cal_sum(9, 15)              
cal_sum(6, 4)              
cal_sum(13, 3)              



def cal_sub(e, o):
    sub = (e - o)
    print(sub)
    return(sub)

cal_sub (10, 9)



def cal_mult(q, r):
    mult = (q * r)
    print(mult)
#     return(mult)

cal_mult(9, 6)
cal_mult(7, 6)
cal_mult(13, 4)


def cal_avg(a, b, c):
    sum = (a + b + c)
    avg = (sum / 3)
    print(avg)
    return(avg)

cal_avg(4, 7, 17)

# Types of Functions: 

# (1) Built in functions

# print, len, type, range


# (2) User Defined function

# WAF to print the length of list(list is the paramater)

cities = ["Gilgit", "skardu", "Lahore"]

def print_len (cities):
    
    print(len(cities))

print_len(cities)    

# WAF to print the elements of the list in a single line?

cities = ["Gilgit", "skardu", "Lahore"]
heroes = ["thor", "superman", "spiderman", "batman", "shaktiman"]

def print_list(list):
    print_len(list)

def print_len(list):
    for item in list:
        print(item, end=" \n ")

print_list(cities)
print_list(heroes)
print()        

# WAF to print the factorial of n. (n is the perameter)

n = 5

fact = 1

for i in range(1, n+1):
    fact *= i
print(fact) 


def cal_fact(n):
    fact= 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)        



def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(59)


# WAF to convert USD into PKR

def converter(usd_val):
    pkr_val = usd_val * 282
    print(usd_val, "USD = ", pkr_val, "PKR")

converter(50)





def converter(usd_val):
    pkr_val = usd_val * 282
    print(usd_val, "USD : ", pkr_val, "PKR : ")

converter(98)

num = int(input("type the num : "))



i = 0
def num(a):
    for i in num():
       if num = input / 2:
           print("even")
    
num(9) 

num = int(input("Type the num : "))
if(num / 2 == 0):
    print("even")
else:
    print("Odd") 

# WAF to print the string even if the input is even and print string odd if input is odd



