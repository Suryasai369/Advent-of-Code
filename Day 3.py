import re
def inp():
    with open("input.txt") as f:
        return f.readlines()
data = str(inp())

#data="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
def mul(data):
    ans = 0
    t = re.findall("mul\(\d*,\d*\)", data)
    for i in t:
        c=0
        for j in range(len(i)):
            if i[j]==",":
                c=j
        n1=int(i[4:c])
        n2=int(i[c+1:len(i)-1])
        ans+=n1*n2
    return ans

def dodn(data):
    while True:
        if re.search(r"don't\(\)", data) == None:
            break
        else:
            donw=re.search(r"don't\(\)", data)
            te=data[donw.end():]
            doni=donw.end()
            dow=re.search("do\(\)", te)
            doi=dow.start()
        data=data[:doni-7]+data[doni+doi+4:]
    print(mul(data))
            


dodn(data)