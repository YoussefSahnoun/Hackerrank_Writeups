from collections import Counter
def nonDivisibleSubset(k, s):
    if k == 1 and len(s) >= 1:
        return 1
    if k == 0:
        return len(set(s))
    
    reminders=[i%k for i in s]
    occ=Counter(reminders)
    prio=reversed(sorted(occ.items(), key=lambda x:x[1]))
    print(prio)
    ct=[]
    result=0
    for i in prio:
        print(i)
        if (k-i[0]%k)%k not in ct and i[0]!=0 and i[0]*2!=k: 
            ct.append(i[0])
            result+=i[1]
    print(ct)
    if 0 in  reminders :
        print('yes')
        result+=1
    if k%2==0 and k/2 in reminders:
        print('yes')
        result+=1
    return result