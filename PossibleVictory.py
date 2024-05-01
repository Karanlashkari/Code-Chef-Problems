r, o, c = map(int,input().split())
a = ((20 - o) * 6) * 6
if (a + c) > r :
    print("YES")
else :
    print("NO")