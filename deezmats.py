

a,b = map(int, input().split())

for i in range(int(a/2)):
    first = "-"*( int((b-3)/2) - i*(3)) +".|"+"..|"*i+"..|"*i+"."+ "-"*( int((b-3)/2) - i*(3))
    if first.startswith("."):
        pass
    else:
        print(first)
print(("-"*(int((b-7)/2)))+"WELCOME"+("-"*(int((b-7)/2))))
for i in range( int(a/2),-1,-1):
    second = "-"*( int((b-3)/2) - i*(3)) +".|"+"..|"*i+"..|"*i+"."+ "-"*( int((b-3)/2) - i*(3))
    if second.startswith("."):
        pass
    else:
        print(second)
