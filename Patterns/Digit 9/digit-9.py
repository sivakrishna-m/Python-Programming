N = int(input())
print("* "*N)
for i in range(N-2):
    print("* " + "  "*(N-2) + "*")
print("* "*N)
for i in range(N-2):
    print((N-1)*"  "+ "*")
print("* "*N)