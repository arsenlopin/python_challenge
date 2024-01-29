# #scope
# #modules

# import platform

# # x = platfor.system
# # x = dir(platform)
# #date 
# from datetime import datetime

# x = datetime.now()
# y = datetime(2020, 5, 17)
# # print(x)
# print(x.strftime("%j %U"))

# #JSON 

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)
# print(y[0:-1])


# #pip


# import camelcase

# c = camelcase.CamelCase()

# txt = "hello ya om peter"

# print(dir(c),c.hump(txt))


# #Errors 
# try:
    
#   print(ddx)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong") 
# finally:
#   print("The 'try except' is finished") 

# x = 1

# if x < 0:
#   raise NameError("Sorry, no numbers below zero") 


# #Files







# x = open("day_seven.py", 'w')
# x.write('hello peter')
# x.close()
# x = open("day_seven.py", 'r')
# print(x.readline())




#challenges of day

# def x(n):
#     print(-n)

# x(10)

# from operator import neg as opposite


#Task 2
# def square_sum(numbers):
# 	res = 0
# 	for num in numbers:
#    		res = res + num*num
# 	return res
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)


#Task 3
	# return 'Odd' if number % 2 else 'Even'
    # like 
    #   return ["Even", "Odd"][number % 2]/
    
