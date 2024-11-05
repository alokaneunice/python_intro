sheep=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

sheepcount=0
presentsheep=[]
def count_sheeps():
    
    for i in sheep:
        if i ==True: #meaning present
            sheepcount=sheepcount=+1
            presentsheep.append(i)
            
        else:
            continue
    print(presentsheep.count(i)) 
    
 # call the function for the final outcome
 # call the function for the final outcome
count_sheeps()