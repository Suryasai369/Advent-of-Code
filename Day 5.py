from collections import defaultdict


#----------Start of input code----------#

def inp(file):
    with open(file) as f:
        return f.readlines()
data = []
rules = []
rdata = inp("input.txt")
rrules = inp("rules.txt")
for i in rdata:
    #data.append(i[:-1])
    data.append(list(map(int,i.split(","))))
for i in rrules:
    rules.append(i[:-1])

r=defaultdict(list)
for i in rules:
    be,af=i.split("|")
    r[int(be)].append(int(af))

#----------End of input code-----------#




#----------Global elements-----------------#

rans,wans=[],[] 
gcount=0

#----------End of global elements----------#






#----------Functions definitions----------#
def crr_data(data):
    l=list(map(int,data.split(",")))
    sa=True
    for j in range(len(l)):
        for k in r[l[j]]:
            if k in l[:j]:
                sa=False
                break
    return sa

def cal(data):
    mi=0
    for i in data:
        i=i.split(",")
        mi+=int(i[(len(i))//2])
    return mi

def chkdata(data):
    for i in data:
        if crr_data(i):
            rans.append(i)
        else:
            wans.append(i)
    return cal(rans)

def wr_to_cr(ri):
    i=list(map(int,ri.split(",")))
    te=i[::]
    don = False
    while True:
        cch=''
        for j in range(len(i)):
            for kk in r[int(i[j])]:
                # print(r[int(i[j])])
                # print("rule:-",i[j])
                # print("k out:-",kk)
                if len(r[int(i[j])])==0:
                    continue
                if kk in i[:j]:
                    #print("k is",kk)
                    ind = i.index(kk)
                    #print("checking ",i[j]," found ",kk," at ",ind)
                    #print(i[j])
                    #print("before:-",i)
                    i.insert(ind,i[j])
                    i.pop(j+1)
                    ch=""
                    for x in i:
                        ch+=str(x)+","
                    #print("checker:-",ch)
                    if crr_data(ch.rstrip(",")):
                        don=True
                    #print("After:-",i)
            if don==True:
                return i
        if crr_data(ri):
            gcount+=1
            print(i,gcount)
            return i
        else:
            for x in i:
                cch+=str(x)+","
            return wans.append(cch.rstrip(","))
        



#----------End of function definitions----------#

# fans=[]
# sfans=[]
# print(chkdata(data))
# print("completed checking")
# #print(wans)
# for i in wans:
#     if wr_to_cr(i)==None:
#         continue
#     fans.append(wr_to_cr(i))

# print("Completed WANS")

# for i in fans:
#     ss=""
#     for j in i:
#         ss+=str(j)+","
#     sfans.append(ss.rstrip(","))
# print("completed Sfans")
# print(cal(sfans))

#print(data)
part1=0
part2=0
for pages in data:
    sorted_pages = sorted(pages, key=lambda page: -len([order for order in r[page] if order in pages]))
    if pages == sorted_pages:
        part1 += pages[len(pages)//2]
    else:
        part2 += sorted_pages[len(sorted_pages)//2]
print(part1)
print(part2)
    

