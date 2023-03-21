n = int(input("enter a number: "))
if n > 2 :
    for i in range(2,n-1):
        if n % i == 0 :
            print("not Prime")
    else:
            print("Prime")
elif n== 2:
    print("Prime")
else:
    print("not Prime")
