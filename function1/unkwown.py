Q_list=(1,4,8,13,15,26,18,19,23,25,34,56,79,90)
        
othervalues=[]
threshold=100
 

#Now it appears the specific numbers 15 and 34 appears in index 6 and 11 in the Q_list given
#write a funtion inside you have the two loops
 
def find(unknown_no):
    for i in Q_list[6:12]:
        #print(i)
        if i==unknown_no:
            final_outcome=i*threshold
            break
        else:
            othervalues.append(i)
            print(othervalues)
    print(final_outcome)
    
#call the function here  and insert the parameter   
find(18)
