def fizzbuzz():
    i=1
    while i<=100:
        if i%3==0 and i%5==0:
            print("fizzbuzz")
            i=i+1
        elif i%3==0:
            print("fizz")
            i=i+1
        elif i%5==0:
            print("buzz")
            i=i+1
        else:
            print(i)
            i=i+1
fizzbuzz()