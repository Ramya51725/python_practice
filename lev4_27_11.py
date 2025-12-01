def prime_no(a,b):
    for i in range(a,b+1):
        s=[]
        for j in range(1,i+1):
            if i%j == 0:
                s.append(j)
        if len(s) == 2:
            print(i)
prime_no(1,15)


def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()    
pattern(5)

nums =  [4,6,9,2,3,11]
k = 2
value=[]
for i in range (-(k),len(nums)):
    value.append(nums[i])
sum=[]
for i in value:
    if i not in sum:
        sum.append(i)
print(sum)


def divisibleSumPairs(ar,k):
    tot=[]
    s=[]
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if i<j :
                add = ar[i] + ar[j]
                if add%k == 0:
                   s.append(ar[i])
                   s.append(ar[j])
                   tot.append(s)
                   s=[]
    print(tot)
    print(len(tot))
divisibleSumPairs([1, 3, 2, 6, 1, 2],3)




def countApplesAndOranges(s, t, a, b, apples, oranges):
    p=[]
    for i in apples:
        sum = a + i 
        p.append(sum)
    o=[]
    for i in oranges:
        sum = b + i 
        o.append(sum)
    app = []
    ora = []
    for k in range(s,t+1):
        for j in range(len(p)):
            if k == p[j]:
                app.append(p[j])
            elif k == o[j]:
                ora.append(o[j])
    print(len(app))
    print(len(ora))
countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])