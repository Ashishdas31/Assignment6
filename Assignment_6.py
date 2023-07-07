# Ans.1
import keyword
print(keyword.kwlist)

# Ans. 9
def fun(n):
 k=n-1
 for i in range(0,n):

    for j in range(0,k):
        print(" ",end="")

    k=k-1

    for j in range(0,i+1):
        print("* ",end="")

    print("\r")

n=7
fun(n)

print(" ")
n=7

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n):
        print("| ",end="")
    n=n-1
    print("\r")




