#How to find  fibonacci number(upto 1000 term)
previous={0:0,1:1}
def fibonacci(n):
    if n in previous:
        return previous[n]
    else:
        new_value=fibonacci(n-1)+fibonacci(n-2)
        previous[n]=new_value
        return new_value
n=int(input("Enter the value of n:"))
print(fibonacci(n))

#Sample output
Enter the value of n:400
176023680645013966468226945392411250770384383304492191886725992896575345044216019675



