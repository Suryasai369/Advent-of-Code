import re
def inp():
    with open("input.txt") as f:
        return f.readlines()

rdata = inp()
data=[]
for i in rdata:
    data.append(i[:-2])
#print(data)
h,w=len(rdata),len(rdata[0])-1
t="XMAS"
c=0
grid = {(y,x):rdata[y][x] for y in range(h) for x in range(w)}
deltas = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
for y,x in grid:
    for dy,dx in deltas:
        can = "".join(grid.get((y+dy*i,x+dx*i),"") for i in range(len(t)))
        #c+= can == t

for y,x in grid:
    if grid[y,x]=="A":
        lr=grid.get((y-1,x-1),'')+grid.get((y+1,x+1),'')
        rl=grid.get((y-1,x+1),'')+grid.get((y+1,x-1),'')
        c += {lr,rl} <= {"MS","SM"}
print(c)


        


