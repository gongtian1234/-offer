'''
题目：输入n个数，找出其中最小的k个数。例如，输入4 5 1 6 2 7 3 8这8个数字，则最小的4个数字是1 2 3 4
（这个题主要是考察时间复杂度；知识点：最大最小堆）

提示：找k个最小的数，需要用到最大堆；找k个最小的数，需要用到最小堆；最大最小堆必须是一个完全二叉树；堆插入一个值的时间复杂度为O(lgn), 删除一个
值得时间复杂度为O(lgn), 创建一个堆的时间复杂度为O(n); 完全二叉树找到其父节点的索引的公式为(index-1)//2，index为当前值的索引，注这里的索引顺序是
按照广度优先排序的，反过来也可以找到其子节点，左子节点索引为index*2+1, 右子节点索引为index*2+2, 

思路：
①可以使用各种排序算法，先对数组进行排序，然后再选出最小的k个数（但是如果数据达到亿级别时，直接排序可能内存放不下）
②借鉴最大最小堆的思路进行解题，要找k个最小的数，首先需要建立一个含有k个数的最大堆，然后再依次遍历去修改已经建立好的最大堆。最大堆并不需要建立真
实的一棵树，而是根据最大堆是完全二叉树的一些性质，将数放在列表里面即可（这种方法的时间复杂度为O(nlogk)）
'''

def getKListNums(tinput, k):
    MaxHeap = []

    def createMaxHeap(num):
        # 创建最大堆，首先是要将数字添加到末尾，然后再让其与其父节点进行比较，如果大于父节点则交换位置
        MaxHeap.append(num)        
        index = len(MaxHeap)-1
        while index!=0:
            parentIndex = (index-1)//2
            if MaxHeap[parentIndex]<MaxHeap[index]:
                MaxHeap[parentIndex], MaxHeap[index] = MaxHeap[index], MaxHeap[parentIndex]
                index = parentIndex
            else:
                break

    def adjustMaxHeap(num):
        if num<MaxHeap[0]:    # 当元素小于最大堆的最大元素，才进入
            MaxHeap[0] = num
            index = 0
            MaxHeapLen = len(MaxHeap)

            while index<MaxHeapLen:
                leftChildIndex = 2*index + 1
                rightChildIndex = 2*index + 2
                # 可能没有右孩，可能左右孩都没有，可能都有
                if rightChildIndex<MaxHeapLen:    # 左右子孩都有
                    if MaxHeap[index]<MaxHeap[rightChildIndex]:
                        MaxHeap[index], MaxHeap[rightChildIndex] = MaxHeap[rightChildIndex], MaxHeap[index]
                        index = rightChildIndex
                    elif MaxHeap[index]<MaxHeap[leftChildIndex]:
                        MaxHeap[index], MaxHeap[leftChildIndex] = MaxHeap[leftChildIndex], MaxHeap[index]
                        index = leftChildIndex
                    else:
                        break
                elif leftChildIndex<MaxHeapLen:  # 只有左孩
                    if MaxHeap[index]<MaxHeap[leftChildIndex]:
                        MaxHeap[index], MaxHeap[leftChildIndex] = MaxHeap[leftChildIndex], MaxHeap[index]
                        index = leftChildIndex
                    else:
                        break
                else:                           # 左右子孩都没有
                    break

    if len(tinput)<k or k<1:
        return []

    for i in range(len(tinput)):
        if i<k:
            createMaxHeap(tinput[i])
        else:
            adjustMaxHeap(tinput[i])
    MaxHeap.sort()
    return MaxHeap

print(getKListNums([1,2,3,4,5,6,7,8,9], 5))