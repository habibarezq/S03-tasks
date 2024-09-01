
def rob( nums: list[int]) -> int:
    prev, cur = 0, 0
    for n in nums:
        print(n)
        temp = max(n + prev, cur)
        prev =  cur
        cur = temp
    return cur
#uses dynamic programming to keep track of money stolen til previous house and current if it's better we rob it else we skip it
n=[0,1,1,3]
print(rob(n))