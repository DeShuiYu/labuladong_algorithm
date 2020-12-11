def trap(height:list):
    n = len(height)
    ans = 0
    for i in range(1,n-1):
        # l_max,r_max = 0,0
        l_max = max(height[:i+1])
        r_max = max(height[i:])
        # for j in range(i,n):
        #     r_max = max(r_max,height[j])
        # for j in range(i,-1,-1):
        #     l_max = max(l_max,height[j])
        ans += min(l_max,r_max)-height[i]

    return ans


print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6