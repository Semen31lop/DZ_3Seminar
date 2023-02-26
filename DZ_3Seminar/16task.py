n=int(input(':'))
x=int(input(':'))
print(n)
list_1=[i for i in range (1,n+1)]
print(list_1)
for i in range(n) :
   count=0
   if x==i:
      count+=1
      print(x)
      print(f' -> {count}')
