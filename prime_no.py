def primeno(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            return
    print(n,"is a Prime number")
    return
n=int(input("Enter No."))
primeno(n)
