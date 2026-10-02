def smallestWindow(str):
    zeros=0
    ones=0
    twos=0
    smallest_sum=0
    k=3
    for i in range(len(str)):
        temp=0
        zeros=0
        ones=0
        twos=0
        for j in range(i,i+k):
            if int(str[j])==0:
                zeros+=1
            elif str[j]==1:
                ones+=1
            else:
                twos+=1
            temp=temp+int(str[j])
        if (zeros==1 and ones ==1 and twos==1) and smallest_sum<=temp:
            smallest_sum=temp
    return smallest_sum

str="01212"
r=smallestWindow(str)
print(r)