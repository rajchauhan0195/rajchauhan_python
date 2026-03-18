#1.Basic Keyword Arguments.
def simple_interest(p:float,t:float,r:float):
    si=(p*r*t)/100
    print("simple interest:",si) 
#calling function.
simple_interest(p=10000,t= 2.5,r=3.5)