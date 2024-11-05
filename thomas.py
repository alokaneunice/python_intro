#Mr Thomas has four props valued at 100000 naira each 
#his father gave him 50000 
#his mum gave him 150000 
#He bought a car ata 200000 
#he gave his wife 30000, if the money in his account initially is 300000
#Write a python code that will show how much he has in his account

def thomas():
    p=100000*4
    f=50000
    m=150000
    c=200000
    w=30000
    i=300000
    balance=(p+f+m+i)-(c+w)
    print("The balance in his account is", balance)
thomas()    