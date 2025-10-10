def lcm (a,b):
    if a>b :
        greater=a
    else :
        greater=b 
    while True:
            if greater%a==0 and greater%b==0:
                  return greater
            greater=greater+1
print (lcm(2,6))