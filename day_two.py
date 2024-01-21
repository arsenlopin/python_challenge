#Today Goals:
# [1]- strings

txt = "hello second day!"
scamtxt = "hello......,,..rrgggrr..banana..hello"

dic  = ("keep","coding")

# txtUpdated = " ".join(dic) #just dicts and tuples are allowed 
# txtUpdated = txt.rpartition('second') => ('hello ', 'second', ' day!')
# txtUpdated = txt.rsplit(' ',1) #=> ['hello', 'second', 'day!']
# txtUpdated = scamtxt.strip("hello,.rg") 
# txtUpdated = txt.zfill(20) #=> 00000hello second day!

#bool

#bool(None) [any empty value] = false

#lists 

# arr = ["1",2,3,4,5]
# del arr[1],arr[0]
# print(arr)


#Today's Challenges 
# [1] -  https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

#my solution
def sum_mix(arr):
    sum = 0
    for n in arr:
         sum = sum + int(n)
    return sum

#best solution
    return sum(int(n) for n in arr)

#other solution
def sum_mix(arr):
 return sum(map(int, arr))




#  Task 2

#my solution
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product


#best solution
import math
def grow(arr):
    return math.prod(arr)
#other solution
def grow(arr):
    return reduce(mul, arr, 1)

#freaking solution
from math import prod as grow