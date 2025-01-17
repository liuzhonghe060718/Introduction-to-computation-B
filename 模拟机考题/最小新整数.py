t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=[]
    nums=list(str(n))

    while len(s)<k:
        p=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                s.append(i)
                p+=1
            if p==k:
                break
        if p==0:
            nums=nums[:len(nums)-(k-len(s))]
            break
        for j in range(1,p+1):
            nums.pop(s[-j])
    print(''.join(nums))

