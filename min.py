1) to find the minimum

def minimum(a):
    min=a[0]
    for i in a:
        if i<min:
            min=i 
    return min 
print(minimum([8,7,1,2,5]))



2) to find the character of string

def char (a,b):
    for i in a:
        if i==b:
            return "Found"
    return "Not Found"
print(char("Helloworld","e"))




3) to count the positive negative and zero number


def count(a):
    positive=0
    negative=0
    zero=0
    for i in a:
        if i==0:
            positive+=+1 
        elif i<0:
            negative+=1
        elif i>0:
            zero+=1
    print(positive)
    print(negative)
    print(zero)
count([5,8,-1,-6,0])


4) to change the first letter and last letter of the name


def name(a):
    a = list(a)
    temp = a[0]
    a[0] = a[-1]
    a[-1] = temp
    b= ''.join(a)
    print(b)
name("ramya")



5) count the length of the list without using the len function


def length(n):
    count=0
    for i in n:
        count=count+1
    print(count)
length([1,2,3,4,5])



6) square the  list and reverse the list


def square(a):
    total=[]
    for i in a:
       sum=i**2
       total.append(sum)
    rev=[]
    for i in range(len(total)-1,-1,-1):
        rev.append(total[i])
    print(rev)
square([1,2,3,4,5])