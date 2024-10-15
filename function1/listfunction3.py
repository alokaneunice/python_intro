# Write a python code that will add list of numbers together
list1=[1,2,4,6,7,9,10]
x=0
threshold=13
basket=[]
for i in list1:
    #print(i)
    x=x+i
    #print(x)
    if x>=threshold:
        #print(x)
        basket.append(x)
        print(basket)