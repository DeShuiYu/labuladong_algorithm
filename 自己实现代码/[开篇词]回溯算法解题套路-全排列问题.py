'''
for 选择 in 选择列表：
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径，选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择在加入选择列表
'''
res = []
import copy

def permute(nums:list):
    track = []
    backtrack(nums,track)
    return res

def backtrack(nums:list,track:list):
    if len(track) == len(nums):
        res.append(copy.deepcopy(track))
        return
    for i in range(len(nums)):
        if track.count(nums[i]) > 0:
            continue
        track.append(nums[i])
        backtrack(nums,track)
        track.pop()

permute([1,2,3,4])
print(res)
