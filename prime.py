def prime(num):
    if num==1:
        print("prime")
    else:
        i=2
        for i in range(i,num+1):
            if num%i==0:
                return "false"
        return "true"
print (prime(9))
 