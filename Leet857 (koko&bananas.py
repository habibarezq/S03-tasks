def minEatingSpeed(piles,h):
    low,high=1,max(piles)
    piles.sort()
    def feasible(k:int):
        time=0
        i=0
        while(i<len(piles)):
            time += (piles[i] + k - 1) // k  
            i+=1
        if(time<=h):
            return True
        else:
            return False
    
    while(low<=high):
        mid=(low+high)//2
        print(low,high,mid)
        if feasible(mid):
            high=mid-1
        else:
            low=mid+1
    return low
