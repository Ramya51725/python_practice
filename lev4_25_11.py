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



def mat(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
            pirnt(a[j])
            

mat([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[9, 8, 7],[6, 5, 4],[3, 2, 1]])