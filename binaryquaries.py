
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    m,n,o=map(int,input().split())
    if x==1:
        a.remove(a[y-1])
        a.insert(1,y-1)
        print(a)
    if m==0:
        s=''
        for i in range(0,o):
            s+=str(a[i])
        z=int(s,2)
        if z%2==0:
            print("EVEN")
        else:
            print("ODD")
