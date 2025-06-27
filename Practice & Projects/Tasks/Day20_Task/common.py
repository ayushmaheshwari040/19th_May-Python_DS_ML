
def isPrime(x):
    if x==1: 
        return f"{x} is not prime no."
    for i in range(2,x): 
        if x%i==0: 
            return f"{x} is not prime no."
    else:
        return f"{x} is a prime no."

def isArmstrong(x): 
    x1=x
    s=0
    while x>0:
        r=x%10
        s=s+r**3
        x=x//10
    if x1==s: 
        return f"{x1} is an armstrong no."
    else: 
        return f"{x1} is not armstrong no."

def isPalindrome(x):
    x1=x
    s=0
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    if x1==s: 
        return f"{x1} is a palindrome no."
    else: 
        return f"{x1} is not palindrome no."
