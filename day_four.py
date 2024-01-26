# Day Four 

#[1] - if and short if (Conditional Expressions|ternary operators)
#[2] - functions 
#[3] - lambada
#[4] - loops



# make a lottary game

# candidates = { 'ali','usery','mohamed', 'ibrahim', "hanny","joe","sanny"}
# lottery_name = {'mohamed','ibrahim','hanny'}
# winner= lottery_name.pop()
# your_name = input("Please enter your name :")

# print("horray!, you are the fucking winner") if your_name in candidates and your_name == winner else print("sorry, your name reached finals but you are not the winner") if your_name in lottery_name and your_name != winner else print("sorry, your name just did not reach to simifinalls") if your_name in candidates else print("your name does not exist.")

#loops


# old_x = ''
# for x in range(0,100,2):
#     if x%10 == 0:
#         old_x = old_x + str("-")
#     old_x = old_x + str(x)
# else:
#   print(old_x) 



# Note: The else block will NOT be executed if the loop is stopped by a break statement.


# Funcs

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus") 

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes") 



#Lambada
# x = lambda n:print(n+7)
# x(8)

# def myfunc(n):
#   return lambda a : (a * n)

# my = (myfunc(3))
# print(my(3))

# def func2(n):
#     def func3(a):
#         return n*a
 
#     my = func3(3)
#     return my

# print(func2(3))

# def func(dec):
#     # temp = ''
#     # # for x in range(0,dec+1):
#     # #     temp += str(x%2)
#     # # print(temp)
#     # i = dec+1
#     # while i > 0 :
#     #     print(i)
#     #     i = i/2









#     return bin(dec)[2:]



# print(func(47))


# print(format(2, 'b'))
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(47)


# Reveivv
# def find_highest_power_2(num):
#     n=0
#     while 2**n <= num:
#         n += 1
#     return n-1    

# def add_binary(a,b):
#     sum = a + b
#     number = 0
#     while sum != 0:
#         place_holder = find_highest_power_2(sum)
#         number += 10**place_holder
#         sum = sum - 2**place_holder
#     return str(number)     




#Taks 2

def get_sum(a,b):
    sum = 0
    if a == b:
        sum = b
    elif a > b:
        for x in range(b,a+1):sum += x
    else:
        for x in range(a,b+1):sum += x
    return sum
print(get_sum(1,0))


# best one 
def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))

#great
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))