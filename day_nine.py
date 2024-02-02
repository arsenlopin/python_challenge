def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")
#nice 
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"
#another 
def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"
def greet(name, owner):
    return 'Hello '+['guest','boss'][name==owner]

def greet(name, owner):
    return 'Hello %s' % ['guest', 'boss'][name==owner]






def num(b):
    number = "".join(map(str, b))
    y = "({}) {}-{}".format(number[0:3],number[3:6],number[6:10])
    print((y))
    return
num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
#best
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
