n=int (input(':'))
x=int(input(':'))
list=[i for i in range (0,n+1)]
for i in range(n):
    if i==x:
        print(x)
    else:
        if x<1:
            print(1)
        else:
            if x>n:
                print(n)
