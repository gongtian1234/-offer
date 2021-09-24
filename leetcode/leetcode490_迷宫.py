# 题目路径：无，因为这道题是会员题目
# 从网上找的有题目的文章：https://blog.csdn.net/wf0934/article/details/103742283

def dfs_helper(arr, start, dest, visit):
    i, j = start[0], start[1]
    if arr[i][j] == 1:
        return False
    if visit[i][j] == 1:
        return False
    if i == dest[0] and j == dest[1]:
        return True
    visit[i][j] = 1
    # 上下左右移动
    if i - 1 >= 0:
        if dfs_helper(arr, (i-1, j), dest, visit):
            return True
    if i + 1 < len(arr):
        if dfs_helper(arr, (i + 1, j), dest, visit):
            return True
    if j - 1 >= 0:
        if dfs_helper(arr, (i, j - 1), dest, visit):
            return True
    if j + 1 < len(arr[0]):
        if dfs_helper(arr, (i, j + 1), dest, visit):
            return True
    return False
        

def solution(arr, start, destination):
    m, n = len(arr), len(arr[0])
    visit = [[0 for _ in range(n)] for _ in range(m)]
    return dfs_helper(arr, start, destination, visit)
