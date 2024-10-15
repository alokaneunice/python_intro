# list1 - Write a python code to multiply list of numbers together using function
list=[11,12,13,14,15,16]
def functionlist():
    total=1
    for i in list:
        total=total*i
        f=total/50
    print("This is my final result" + str(f))
    #you can also use this
    print("This is my final result",f)
functionlist()