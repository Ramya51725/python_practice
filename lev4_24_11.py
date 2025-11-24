# 1. Pattern Printing – Stars

# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# pattern(4)


# 2. Multiplication Table (1–5)

# def multiply(n):
#     for i in range(1,n+1):
#         for j in range(1,11):
#             print(i,"X",j,"=",i*j)
#         print()
# multiply(5)

# 3. Student Marks Table

# def student(a,b):
#     for i in range (len(a)):
#         for j in range(len(b)):
#             print(a[i],b[j])
#         print() 
# student(["Arun", "Priya", "Kiran"],["Math", "Science", "English"])


# 4. Pair Sum Finder

# def pair(a):
#     for i in range(len(a)):
#         for j in range (i+1,len(a)):
#             print(a[i],"+",a[j],"=",a[i]+a[j])
# pair([2, 4, 6])


# Vowel Count in Multiple Words

# def words(a):
#     for i in range(len(a)):
#         count = 0
#         for j in range (len(a[i])):
#             if a[i][j] == "a" or a[i][j] == "e" or a[i][j] == "i" or a[i][j] == "o" or a[i][j] == "u":
#                 count=count+1
#         print(a[i],">>",count)
# words(["apple", "banana", "pear"])

# 6. Matrix Elements

# def matrix(a):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             print(a[i][j],end=" ")
#         print()
# matrix(([1, 2, 3],[4, 5, 6],[7, 8, 9]))



# 7. Common Letters Between Words

# def lis(a,b):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] in b[j]:
#                 print(a[i],">>",b[j])
# lis(["bat", "ball"],["apple", "balloon"])


# 8. Duplicate Characters in Words

# def duplicate(a):
#     for i in range(len(a)):
#         seen=[]
#         k=[]
#         for j in range(len(a[i])):
#             if a[i][j] not in seen:
#                 seen.append(a[i][j])
#             else:
#                 k.append(a[i][j])
#         h=[]
#         for t in range (len(k)):
#             if k[t] not in h:
#                 h.append(k[t])
#         print(a[i],">>",h)
# duplicate(["success", "letter", "banana"])

