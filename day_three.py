

# Today's Goals
# [1] - Data types finished 


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 =  list2 + list1
# list3.reverse()
# list3.clear()
# list3 = list1.copy()
# list3.insert(1,list1[1])

# print(list3.count('b')) 



# Tuples

# mytuple = ("apple", "banana", "cherry") 
# thistuple = ("apple", "banana")
# thistuple + mytuple
# print(thistuple,mytuple)


#unpacking 

# fruits = ("apple","dd", "banana", "cherry")

# (green, *yellow, red) = fruits

# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 10

# x = mytuple.index('apple')

# print(x) 

#Sets

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# thisset.update([1,2,3,4,5])
#  #dublcated value is ignored 1 = true 
# thisset.discard(1)
# randomele = thisset.pop()
# print('the random looser is %s' % randomele) 


# car1 = {
# "brand": "Ford",
# "model": "Mustang",
# "year": "1964"
# }

# car2 = {
# "brand": "verna",
# "model": "toskan",
# "year": "1974"

# }
# car3 = {
# "brand": "toyta",
# "model": "krola",
# "year": "2007"
# }

# cars = dict({"car1":car1, "car2":car2, "car3":car3})
# print(cars)
# print(x) #before the change

# car["hi"] = 2020
# car.update({'sol': 2021})
# car.pop('year') | del car['model']

# for hi in car:
#     txt = "your car's {} is {}".format(hi,car[hi])
#     print(txt) #after the change 

# for car in cars:
#     print(car)

#Task One 

# def boolean_to_string(b):
#     return str(b)


#Task Two
# In this little assignment you are given a string of space separated numbers,
#  and have to return the highest and lowest number. 
#  # REQUIREMENTS # There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, 
# #  and highest number is first. 

# def high_and_low(numbers):
#     str_to_list = numbers.split()
#     list_of_numbers = [int(number) for number in str_to_list]
#     # sorting the numbers 
#     list_of_numbers.sort()
#     # get the 2 values 
#     lowest_number = str(list_of_numbers[0])
#     highest_number = str(list_of_numbers[-1])
#     # return them in last form 
#     result = highest_number+" "+ lowest_number
#     return result

#second one 


# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])
# high_and_low("1 2 9 -1 4 5")

# best parctice 

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" %(max(nn),min(nn))