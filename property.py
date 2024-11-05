#Python code for properties
#mr Kolade had three properties valued at 21,000 each
#mr kolade's friend gave him another  two properties val at 41,000 each
#unfortunately he had a business dealing and lost 35,000
#Write a python function code that determines how much mr kolade is valued now

def Kolade():
    p = 21000*3
    f = 41000*2
    d = 35000
    balance = p+f-d
    print("This is Mr Kolade's balance ", balance)
Kolade()    