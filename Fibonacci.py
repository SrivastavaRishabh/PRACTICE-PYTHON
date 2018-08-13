def fibo(num):
    if num == 1:
        print("1")
    elif num == 2:
        print("1 1")
    else:
        a,b,c=1,1,0
        fib=[]
        fib.append(a)
        fib.append(b)
        for i in range(num-2):
            c=a+b
            fib.append(c)
            a,b=b,c
        print(tuple(fib))

num = int(input("Enter the limit of fibonacci series : "))
fibo(num)