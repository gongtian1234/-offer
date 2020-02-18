'''
题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n), 空间复杂度是O(1)
(这个题目比较难，难以口述清除，要结合代码进行理解)

思路：
使用异或这个位运算进行解题（首先异或运算也具有交换律）。
因为数组中除了两个只出现依次的数字外，其他的数字都是出现了两次，使用异或运算可以使出现两次的数字的异或结果为0(如(1,1,2,2,3,4,4,5,5,6), 
整体进行异或后，结果为5==101)，从而找出两个只出现一次数字的异或结果x，再找到x的二进制码中1首次出现的位置，并截取其右半段为y（如5的右半段为1，
再如异或结果为20==10100，截取的右半段为100）；再用截取的右半段y与数组中的每个数字进行与操作，可以将数组分为两段，并且每段中有一个只出现一次的
数字，再分别对每段进行异或操作，从而找到了两个只出现一次的数字
'''
def findNumsAppearOnce(nums):
    if len(nums)<2:
        return None

    twoNumsXor = None
    for num in nums:
        if twoNumsXor is None:
            twoNumsXor = num
        else:
            twoNumsXor = twoNumsXor ^ num
    
    count = 0                         # 用来标记twoNumsXor的二进制表示中1首次出现的位置
    while twoNumsXor%2==0:            # 因为要找的是1首先出现的位置，所以只要结果是奇数就满足条件
        count += 1
        twoNumsXor = twoNumsXor//2    # 或者twoNumsXor>>1是一样的
    mask = 1<<count                   # mask相当于是截取出的右半段y

    firstNum = None
    secondNum = None
    for num in nums:
        if mask&num==0:
            if firstNum is None:
                firstNum = num
            else:
                firstNum = firstNum ^ num
        else:
            if secondNum is None:
                secondNum = num
            else:
                secondNum = secondNum ^ num
    return firstNum,secondNum


print(findNumsAppearOnce((1,1,2,2,3,4,4,5,5,6)))