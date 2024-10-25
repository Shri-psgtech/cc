dp=[]

c={}


with open("naive.txt","r") as file:
    while True:
        data=file.readline().strip().split()
        
        dp.append(data)

        if(data[-1]=='-'):
            break
        if data[-1] not in c:
            c[data[-1]]=1
        else:
            c[data[-1]]+=1

dp=dp[1:]
q=dp.pop()
n=len(dp)-1
print(f"size :{n}")
del c['label']

pC=[round((float(c[i])/n),3) for i in c ]
print(pC)
        
q.pop()
count_q=[]

for c_ele in c:
    
    ans=1
    for attribute in range(len(q)):
        count=0
        for data_point in dp:
            if(data_point[attribute] == q[attribute]):
                if(data_point[-1]==c_ele):
                    count+=1
        ans*=count/c[c_ele]
    count_q.append(round(ans,4))
        
print(count_q)


ans=[]

for i in range(len(count_q)):
    ans.append(round(count_q[i]*pC[i],3))
print(ans)
    