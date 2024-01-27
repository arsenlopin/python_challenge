# #[1]-classes











# #---------------Classes--------------#

# # class Person: 
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age
# #   def __str__(self):
# #     return f"{self.name},{self.age}"
# #   def functions(f,*y):
# #     print(f)

# # p1 = Person("John", 36)
# # del p1.functions 
# # p1.functions()





# #------------inheritance------------

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname() 

# # class Student(Person):
# #     pass


# class Student(Person):
#   def __init__(self, fname, lname, age):
#     super().__init__(fname, lname) 
#     self.age = age 
#   def sayhi(self): 
#         print(self.firstname)
# u = Student('hanny','mike',34)
# u.sayhi()
# print(u.age)



# challenge 


# my sultion is the best 
def validate_pin(bin):
     bin.isdigit() and len(bin) in [4,6]
     return ''
print(validate_pin('4345'))



# Task 2 


def let(a,b):
     txt,temp_store,result = (a+b),set(()),'' 
     for x in txt:temp_store.update(x)
     temp_store = list(temp_store)
     temp_store.sort()
     for x in temp_store: result+=x 
     print(result)   
    
# fuck me !!!!!!!!!!!!!

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(let('xyaabbbccccdefww',"xxxxyyyyabklmopq"))
