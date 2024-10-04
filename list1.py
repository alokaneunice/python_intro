#python code to add numbers together
list1=[2,50,6,78,34,23,21]
#print(sum(list1))

total=0
for i in list1:
   # print(i)
    total=total + i
print(total)
#check if total is greater than 50, if yes, divide by 20 and add 19. otherwise add 500
if total>50:
    print("Hurray total is greater than 50")
    result=(total/20)+19
    print(result)
else:
    result=total+500