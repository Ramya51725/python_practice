def password(name):
    count=0
    for i in name:
        count=count+1
    for i in name:
        if (i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*') and (count>=8):
            return " Password is strong"
    return ("Password is not strong")
print(password("my@password"))
