N = int(input())
n = N
for i in range(1,N+1):
    row = ""
    for j in range(1,i+1):
        row += str(j) + " "
    print(" "*(n-1) + row)
    n -= 1
n = N
for i in range(1,N):
    row = ""
    for j in range(1,n):
        row += str(j) + " "
    print(" "*i + row)
    n -= 1
