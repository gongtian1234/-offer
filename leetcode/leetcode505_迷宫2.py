def dfs_helper2(arr, start, dest, visit):
    i, j = start[0], start[1]
    m, n = len(arr), len(arr[0])
    if arr[i][j] == 1:
        return False
    if visit[i][j] == 1:
        return False
    if i == dest[0] and j == dest[1]:
        return True
    visit[i][j] = 1
    u = i - 1
    d = i + 1
    l = j - 1
    r = j + 1
    while u >= 0 and arr[u][j] != 1:
        u -= 1
    if dfs_helper2(arr, (u+1, j), dest, visit):
        return True
    while d < m and arr[d][j] != 1:
        d += 1
    if dfs_helper2(arr, (d-1, j), dest, visit):
        return True
    while l >= 0 and arr[i][l] != 1:
        l -= 1
    if dfs_helper2(arr, (i, l+1), dest, visit):
        return True
    while r < n and arr[i][r] != 1:
        r += 1
    if dfs_helper2(arr, (i, r-1), dest, visit):
        return True
    return False


def solution2(arr, start, dest):
    visit = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    return dfs_helper2(arr, start, dest, visit)

arr2 = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
print(solution2(arr2, (0, 3), (4, 4)))
