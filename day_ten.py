# Problem number 20 day 10

def likes(likers):
    names = tuple(likers)
    length_of_names = len(names)
    msgs = (
    "no one likes this",
    f"%s likes this",
    f"%s and %s like this",
    f"%s, %s and %s like this"
    )
    return (msgs[len(names)]%names[0:len(names)]) if length_of_names <= 3 else f"%s, %s and %s others like this"%(*names[0:2],length_of_names-2) 

print(likes(['no','yes','yes','yes','yes','yes','yes','yes']))


#fucking good solution
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

