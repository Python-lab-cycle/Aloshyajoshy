class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name=",self.nam)
        print("acnt num=",self.ac)
        print("acnt type=",self.type)
        print("bal=",self.amount)
    def withl(self,wl):
        return(self.amount-wl)
n=input("Enter name:")
t=input("Enter type:")
a=int(input("Enter numbr:"))
am=int(input("Enter amount:"))
obj=bank(a,n,t,am)
print("Account details")
obj.printamt()
w=int(input("Enter amount to withdraw:"))
print("b1=",obj.withl(w))
