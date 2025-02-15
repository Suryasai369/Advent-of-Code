import re
def inp():
    with open("input.txt") as f:
        return f.readlines()
data = str(inp())
ans=0
'''for i in range(len(data)-8):
    if data[i]=='m' and data[i+1]=='u' and data[i+2]=="l" and data[i+3]=='(' and data[i+4].isnumeric() and data[i+5]==',' and data[i+6].isnumeric() and data[i+7]==')':
        ans+=int(data[i+4])*int(data[i+6])

'''

#data="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
'''
for i in range(len(data)-7):
    if data[i]=='m' and data[i+1]=='u' and data[i+2]=="l" and data[i+3]=='(' and data[i+4].isnumeric() and data[i+5]==',' and data[i+6].isnumeric() and data[i+7]==')':
        print("in")
        print(data[i:i+8])
        ans+=int(data[i+4])*int(data[i+6])
    if i==53:
        print(data[i:i+8])
print(ans)
'''
t = re.findall("mul\(\d*,\d*\)", data)
for i in t:
    c=0
    for j in range(len(i)):
        if i[j]==",":
            c=j
    n1=int(i[4:c])
    n2=int(i[c+1:len(i)-1])
    ans+=n1*n2
print(ans) 