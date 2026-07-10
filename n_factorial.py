def factorial(n):
    s=1
    for i in range (1,(n+1)):
        s=s*i
    return s
n_factorial = factorial (int(input("enter the n :")))
print(n_factorial)
        


    