def merge(intervals: list[list[int]]):
    intervals.sort(key=lambda x:x[0])
    selected=[intervals[0]] 
    for interval in intervals[1:]:
        if interval[0]<=selected[-1][1]: #if start of 2nd one is less than end of 1st one then they are overlapping
            if selected[-1][1]<interval[1]:  #becuz of test case [1,4],[2,3] i want interval [1,4] not [1,3]
                selected[-1][1]=interval[1]  
        else:
            selected.append(interval)
    return selected
#using greedy algorithm 