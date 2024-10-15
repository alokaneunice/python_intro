def calculate():
    a=21
    b=31
    c=41
    d=(a*b*c-500)
    print(d)
    if d>1000:
        print("Yes, it is greater than 1000")
        f=d*30
        print("Yes, this is the final value" + str(f))
    else:
        print("No, it is less than 1000")
        g=d*10
        print("Good, this is the final value" + str(g))

calculate()