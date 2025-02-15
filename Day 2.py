def inp():
    with open("input.txt") as f:
        return f.readlines()
data = inp()

def safe(d):
    i=list(map(int, d.split()))
    s=False
    if i==sorted(i) or i==sorted(i, reverse=True):
        for j in range(len(i)-1):
            if abs(i[j]-i[j+1])>3 or abs(i[j]-i[j+1])==0:
                s=False
                break
        else:
            s=True
    if s:
        return "Yes"

def main():
    ans=0
    for i in data:
        if safe(i):
            ans+=1
        else:
            i=list(map(int, i.split()))
            for j in range(len(i)):
                t=i[:j]+i[j+1:]
                if safe(" ".join(map(str, t))):
                    ans+=1
                    break
    print(ans)
            
    
main()
    
 
'''
i=[8,6,4,4,1]
s=False
if i==sorted(i) or i==sorted(i, reverse=True):
    print("in")
    for j in range(len(i)-1):
        if abs(i[j]-i[j+1])>3 or abs(i[j]-i[j+1])==0:
            s=False
            break
    else:
        s=True
if s:
    print("Yes")
        
'''
            

