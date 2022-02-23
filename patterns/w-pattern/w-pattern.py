N = int(input())
n = 2*N - 1
mid = 1
x = (N-2)
for i in range(N):
    if i == 0 or i == 1:
        print(" "*i+"* "*n)
        n -= 1
    else:
        print(" "*i + "* "*x + "  "*mid + "* "*x)
        mid += 1
        x -= 1