from math import sqrt; s,e=int(input()),int(input()); l=int(-(sqrt(e+1-s)//-1)); g=[[-1for _ in range(l)]for _ in range(l)]; t=(l-1)//2; p,a=[t,t],2
# def f(x,y): global s,e,g,p; g[p[0]][p[1]],p[y],s=s,p[y]+x,s+1; return iter(()) if
while s<=e:
    for x,y in (1,0),(1,1),(-1,0),(-1,1):
        for _ in range(a//2):
            if s>e:break
            else: g[p[0]][p[1]],p[y],s=s,p[y]+x,s+1
        if s>e:break
        else: a+=1
[print(*[""if g[x][y]==-1else g[x][y]for y in range(l)])for x in range(l)]