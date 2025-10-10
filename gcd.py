def gcd (a,b):
    if a<b:
        least=a
    else:
        least=b
    while True:
        if  a%least==0 and b%least==0:
            return least
        least=least-1
print(gcd(42,56))
    