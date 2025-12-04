def num(n):
    for i in range (1,n+1):
        print(" "*(n-i),end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()
num(3)


    
        
num= "The quick brown fox jumped over the quick"
val= "quick"
val=val.lower()
num=num.lower()
for i in range(len(num)):
    if num[i] == val[0]:
        print(i)
        break


def migratoryBirds(arr):
    num = {}
    for i in arr:
        if i in num:
            num[i]= num[i] + 1 
        else:
            num[i] = 1
    large = max(num.values())
    last={}
    for i,j in num.items():
        if j == large:
            last[i] = j 
    end = min(last.keys())
    return end
migratoryBirds([1, 4, 4 ,4, 5, 3])
migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
migratoryBirds([2,2,1,1,3])



def diagonalDifference(arr):
    pri_diagonal = 0
    sec_diagonal = 0
    for i in range(len(arr)):
        pri_diagonal = pri_diagonal+arr[i][i] 
    for i in range (len(arr)):
        sec_diagonal = sec_diagonal + arr[i][-(i+1)]
    if pri_diagonal > sec_diagonal :
        tot = pri_diagonal - sec_diagonal 
    else:
        tot = sec_diagonal - pri_diagonal 
    return tot
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
