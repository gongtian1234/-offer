'''
冒泡排序：
第一轮：从左到右相邻元素比较，较大元素放在后面，第一轮下来，就会把最大的元素放在最右边；
第二轮：从左到n-1个数，会把第二大的数移到倒数第二个位置
依次类推。
时间复杂度为O(n^2), 空间复杂度O(1)(不需要额外的空间)；
冒泡排序是一个稳定的排序方式【稳定：有重复的数字时，如出现在前面的2，排完序后，它还是在前面】；
当数组已经排好序时，可以设置停止条件，如：在一次交换搜索中，并没有发生交换，表明该数组已排好序了，所以需要停止
'''

'''
选择排序：
第一轮，会记录下最大值的索引，最后将最后一个元素与最大值的索引位置处进行交换；
第二轮，找第二大，最后将其与倒数第二个位置交换；
依次类推。
交换次数O(n)，不稳定，费适应（没有办法早停），时间复杂度为O(n^2)
'''

'''
插入排序：
和摸牌类似，边摸牌边将牌放入对应的位置。
拿到第一个数，放在第一个位置；再拿到第二个数，和以一个数比较放在其前或后；再拿到第三个数，与已有的两个数比较放在对应位置，从倒数第一个数比较
如果小于倒数，二者交换位置后，再将其与倒数第二个数比较；
是稳定的，时间复杂度为O(n^2)
'''

'''
希尔排序：
当数组很小时，插入排序是非常快的。插入排序的简单扩展，用到的不是非常多。【希尔排序不会】
'''

'''
上面是几种排序比较慢的方法，下面是几种比较快的方式（计数排序，以及后面的排序方法都非常重要）
计数排序：
适用范围：数字比较集中，即range范围小；有很多重复的数字
首先找到最大值和最小值（也是找到了范围），分配range（max-min+1）个位置，遍历并计数，统计每个数出现的次数，并放在对应的位置，最后展开还原数组
时间复杂度为O(n)，缺点是需要额外的空间（当range范围非常大时，需要的空间较大）
'''

'''
归并排序(采用的是分治算法)：
时间复杂度为nlogn(递归，可以用主项定理进行分析)，空间复杂度为O(n),
改进：对小型子矩阵使用插入排序；测试数组是否已经按顺序排序，如果第一个的最大值已经小于第二个的最小值，此时直接合并就行
'''

'''
快速排序【最重要的排序方式】
(也采用的是分治算法)
快速排序，递归：先找两个指针指向第二个数和最后一个数，两个指针的数分别与第一个数比较，如果cur1指的数大于第一个数，cur2指的数小于第一个数，
让两个指针的数交换位置；如果不满足继续往下找，直到cur1找到大于第一个数和cur2找到小于第一个数，再交换位置【注意：cur1是从左往右找比第一个数
大的数，cur2是从右往左找比第一个数小的数】，直到cur1、cur2出现交集为止。结束一次后，再把第一个数与交集位置的数互换，此时在该数的左边都是小
于它的数，右边都是大于它的数，再使左右两边都进入递归，从而最终实现排序(代码实现的和这个有点不一样，代码是利用了python的优势)
最优时间复杂度O(nlogn)(第一个数刚好在排序后的中间)，最坏时间复杂度为O(n^2)，不需要额外的空间，所以最常使用快速排序
改进：不选择第一个数，每次都选择中间那个数
'''

def bubble_sort(array):
    for i in range(len(array)):
        is_sorted = True   # 停止标记
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                is_sorted = False
            if is_sorted is True:   # 停止条件
                break
    return array
print('bubble_sort: ',bubble_sort([9,8,7,6,5,4,3,2,1,2]))


def selection_sort(array):
    n = len(array)
    for i in range(len(array)):
        max_idx = 0
        for j in range(len(array)-i):
            if array[max_idx]<array[j]:
                max_idx = j
        array[n-i-1], array[max_idx] = array[max_idx], array[n-i-1]
    return array
print('selection_sort:', selection_sort([9,8,7,6,5,4,3,2,1,2]))


def insert_sorted(array):
    n = len(array)
    for i in range(n):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array
print('insert sort: ', insert_sorted([9,8,7,6,5,4,3,2,1,2]))


def count_sort(array):
    n = len(array)
    maxi, mini = array[0], array[0]  # 找到最大值和最小值
    for i in range(n):
        if array[i]>maxi:maxi=array[i]
        elif array[i]<mini:mini=array[i]
    counts = [0]*(maxi-mini+1)       # 分配range个位置
    for i in range(n):               # 遍历并计数
        counts[array[i]-mini] = counts[array[i]-mini] + 1
    pos = 0                          # 为了在array中定位
    for j in range(len(counts)):
        for m in range(counts[j]):
            array[pos] = mini + j
            pos += 1
    return array
print('count sort: ',count_sort([1,1,2,3,6,6,5,4,1,2]))

class MergeSort:
    def _merge(self, a, b):
        ''' 合并列表 '''
        c = []
        while len(a)>0 and len(b)>0:
            if a[0]>b[0]:
                c.append(b[0])
                b.remove(b[0])
            else:
                c.append(a[0])
                a.remove(a[0])
        if len(a)==0:   # 可能一个已经空了，但是另一个还有
            c += b
        else:
            c += a
        return c

    def _merge_sorted(self, arrayi):
        ''' 采用递归的方式拆分 '''
        if len(arrayi)<=1:
            return arrayi
        m = len(arrayi) // 2
        a = self._merge_sorted(arrayi[:m])
        b = self._merge_sorted(arrayi[m:])
        return self._merge(a, b)

    def merge_sort(self,array, reverse=False):
        array = self._merge_sorted(array)
        if reverse:
            array = array[::-1]
        return array
print('merge sort(归并排序)：',end='')
ms = MergeSort()
print(ms.merge_sort([9,8,7,6,5,4,3,2,1,2]))

class QuickSorted:
    def _quick_sorted(self, nums):
        if len(nums)<=1:
            return nums
        pivot = nums[0]
        left_nums = self._quick_sorted([x for x in nums[1:] if x<pivot])
        right_nums = self._quick_sorted([x for x in nums[1:] if x>=pivot])
        return left_nums + [pivot] + right_nums

    def quick_sorted(self, array, reverse=False):
        array = self._quick_sorted(array)
        if reverse:
            array = array[::-1]
        return array
print('quick sorted:', end=' ')
qs = QuickSorted()
print(qs.quick_sorted([9,8,7,6,5,4,3,2,1,2]))

