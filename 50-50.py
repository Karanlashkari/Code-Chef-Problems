T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    if x < 50 :
        print("Z")
    else:
        if y <50 :
            print("F")
        else:
            print("A")