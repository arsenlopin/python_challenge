import time
def reverse_words(text):
    x = "hello  yan"
    y = x.split(" ", )
    result = ''
    for z in y: 
        result += z[::-1] + " "
    print(result.strip())

#best 
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


def su(arr):
    if type(arr) is not list or len(arr) in [0,1,2]:
        return 0
    arr.sort()
    return sum(arr[1:-1])
su([12,174,3,8])

StartTime = (time.strftime('%S'))
def dd(arr):
     return sum(sorted(arr[1:-1])) if arr else 0
print(dd(None))

EndTime = (time.strftime('%H:%M:%S:%Z:%m'))
print(EndTime)
# print(int(EndTime) - int(StartTime))