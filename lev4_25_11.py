1) input  [1,2,3]
output  [1,2][1,3],[2,3]

def lis(a):
    s=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            s.append(a[i])
            s.append(a[j])
            print(s)
            s=[]
lis([1,2,3])



Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

def longest(a):
    for i in range(len(a)):
        print(a[i])
        for j in range()
longest(["flower","flow","flight"])


def mat(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j]+b[i][j],end=" ")
        print()
mat([[1, 2, 3],[4, 5, 6], [8, 7, 6]],[[7, 8, 9],[6,5,4 ], [5, 4, 3]])


sub array

def sub(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            print((a[i],a[j]),end=" ")

sub([1,2,2,3])  

def max_subarray_sum(arr):
    h=[]
    for i in range(len(arr)):
        sum=[]
        for j in range (i,len(arr)):
            sum.append(arr[j])
            print(sum)
            s=[]
            for k in  sum:
                s.append(k)
            h.append(s)
    for i in range (len(h)):
        if len(h[i]) == 2:
            for j in range (len(h[i])):
                if h[j][0] != h[j][-1]:
                    print(h[i])
max_subarray_sum([1,2,3,4])




