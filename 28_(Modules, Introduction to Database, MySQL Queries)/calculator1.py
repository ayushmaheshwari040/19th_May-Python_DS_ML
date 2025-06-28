                                                        # here calculator1.py becomes module now
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

if __name__=='__main__':               # if we write this stateme
    a=int(input("Enter a:"))                       
    b=int(input("Enter b: "))
    print(addition(a,b))
    print(subtraction(a,b))
