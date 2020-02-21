'''
题目：
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值，如果数据流中读出偶数个数值，
那么中位数就是所有数值排序后中间两个数字的平均值。我们使用insert()方法读取数据流，使用getMedia()方法获取当前读取数据流的中位数

思路：
将数组里的数交替放入最大堆最小堆中，这样中位数只能是最大堆的堆顶或者最大最小堆堆顶元素的均值。首先编写最大堆最小堆的创建及修改的函数
（共4个），交替的往最大最小堆添加数字（添加数字的过程是重点），从而保证最大最小堆里的元素个数要么相等，要么相差一个，从而实现了实时获
取数据流的中位数。
'''

class Solution:
    def __init__(self):
        self.littleMaxHeap = []    # 存放小数的最大堆
        self.largeMinHeap = []     # 存放大数的最小堆
        self.littleCount = 0       # 对littleMaxHeap进行计数
        self.largeCount = 0        # 对largeMinHeap进行计数

    def insert(self, num):
        if self.littleCount==self.largeCount==0:    # 刚开始最大最小堆都为空时
            self.littleMaxHeap.append(num)
            self.littleCount += 1
        elif self.littleCount==1 and self.largeCount==0:
            if num>self.littleMaxHeap[0]:
                self.largeMinHeap.append(num)
            else:
                tmp = self.littleMaxHeap.pop()
                self.littleMaxHeap.append(num)
                self.largeMinHeap.append(tmp)
                self.largeCount += 1
        elif self.littleCount==self.largeCount:    # 应该是最大堆增加一个数
            # 5   8     4 6  9
            if num<self.largeMinHeap[0]:
                self.createMaxHeap(num)
            else:
                tmp = self.largeMinHeap[0]
                self.adjustMinHeap(num)
                self.createMaxHeap(tmp)
            self.littleCount += 1
        elif self.littleCount>self.largeCount:    # 应该是最小堆增加一个数
            # 5   8     4  6 9
            if num<self.littleMaxHeap[0]:
                tmp = self.littleMaxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tmp)
            else:
                self.createMinHeap(num)
            self.largeCount += 1
        
        # print('当前的littleMaxHeap为',self.littleMaxHeap)
        # print('当前的largeMinHeap为',self.largeMinHeap)
    def getMedia(self):
        # print('当前的littleCount为',self.littleCount)
        # print('当前的largeCount为',self.largeCount)
        if self.largeCount==self.littleCount:
            return (self.largeMinHeap[0]+self.littleMaxHeap[0])/2
        elif self.largeCount+1==(self.littleCount):
            return (self.littleMaxHeap[0])

    def createMaxHeap(self, num):
        self.littleMaxHeap.append(num)
        index = len(self.littleMaxHeap)-1
        while index>0:
            parentIndex = (index-1)//2
            if self.littleMaxHeap[parentIndex]<self.littleMaxHeap[index]:
                self.littleMaxHeap[index], self.littleMaxHeap[parentIndex] = self.littleMaxHeap[parentIndex],self.littleMaxHeap[index]
                index = parentIndex
            else:
                break

    def adjustMaxHeap(self, num):
        if num<self.littleMaxHeap[0]:
            self.littleMaxHeap[0] = num
            index = 0
            littleLen = len(self.littleMaxHeap)
            while index<littleLen:
                leftChildIndex = index*2+1
                rightChildIndex = index*2+2
                largeIndex = 0
                if rightChildIndex<littleLen:
                    if self.littleMaxHeap[leftChildIndex]<self.littleMaxHeap[rightChildIndex]:
                        largeIndex = rightChildIndex
                    else:
                        largeIndex = leftChildIndex
                elif leftChildIndex<littleLen:
                    largeIndex = leftChildIndex
                else:
                    break

                if self.littleMaxHeap[index]<self.littleMaxHeap[largeIndex]:
                    self.littleMaxHeap[index], self.littleMaxHeap[largeIndex] = self.littleMaxHeap[largeIndex], self.littleMaxHeap[index]
                    index = largeIndex
                else:
                    break


    def createMinHeap(self, num):
        self.largeMinHeap.append(num)
        index = len(self.largeMinHeap) - 1
        while index>0:
            parentIndex = (index-1)//2
            if self.largeMinHeap[index]<self.largeMinHeap[parentIndex]:
                self.largeMinHeap[index],self.largeMinHeap[parentIndex] = self.largeMinHeap[parentIndex], self.largeMinHeap[index]
                index = parentIndex
            else:
                break

    def adjustMinHeap(self, num):
        if self.largeMinHeap[0]<num:
            self.largeMinHeap[0] = num
            index = 0
            largeLen = len(self.largeMinHeap)
            while index<largeLen:
                leftChildIndex = index*2+1
                rightChildIndex = index*2+2
                smallIndex = 0
                if rightChildIndex<largeLen:
                    if self.largeMinHeap[leftChildIndex]<self.largeMinHeap[rightChildIndex]:
                        smallIndex = leftChildIndex
                    else:
                        smallIndex = rightChildIndex
                elif leftChildIndex<largeLen:
                    smallIndex = leftChildIndex
                else:
                    break

                if self.largeMinHeap[smallIndex]<self.largeMinHeap[index]:
                    self.largeMinHeap[smallIndex], self.largeMinHeap[index] = self.largeMinHeap[index], self.largeMinHeap[smallIndex]
                    index = smallIndex
                else:
                    break

if __name__=='__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.insert(i)
        print(s.getMedia())    # [5, 3.5, 3, 3.5, 3, 3.5, 4, 3.5, 4]
