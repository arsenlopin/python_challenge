# Goals
#[1]- variables
#[2]- functions
#[3]- data types 
#[4]- 2 tasks

# import random
# print("  \n hello, world!")
# variables
# note 1 py does not overrite different data types  
# x,y,z = 0,11,3
# X = str(10)
# print(x,X)

#funcs 
# topG = "andrew tate"
# def top_g_me():
    # print("\n \n The Top G Is: " + topG + " \n" )
    # def say_my_name():
    #     print("but now " )
    #     global topG
    #     topG = "Code Chef (You) "
    #     """empt function"""
    #     # print("hi from func")
        
    # # end def
    # say_my_name()
    # print("\n  The Top G Is: " + topG + "\n" )
# top_g_me()

################################################


# print(random.randrange(0,20))

# check value in text
# txt = "      lorem Ips but not {1} enough {0} True" 
# sava = "lorem" not in txt 
# print("yes" if(str(sava) in txt) == 0 else "no")
# print(txt.format("satnder","hu"))




# day challenge # 


# 1- return yes if the bool is true

#my solution
def bool_to_word(bool):
    return "Yes" if bool else "No"
#best solution
def bool_to_word(bool):
    return ['No', 'Yes'][bool]


# 2- return yes if the bool is true
# Write a function that takes an array 
# of numbers and returns the sum of
#  the numbers. The numbers can be
#  negative or non-integer. If 
# the array does not contain any
#  numbers then you should return 0.

Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

#my solution 

def sum_array(a):
    sum = 0 
    for num in a:
         sum = sum + num
    return sum

# best solution
def sum_array(a):
  return sum(a)

# another solution
sum_array = sum


