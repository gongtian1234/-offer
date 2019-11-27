'''
题目：在有空字符串隔开的有序array中查找元素。给定一个有序的字符串序列，这个序列中的字符串用空字符串隔开，请写出找到给定字符串位置的方法。
      如[' ', ' ', 1, ' ', ' ',' ', 2, ' ',3]
思路：
没有什么好的办法，第一种办法直接直接遍历；
第二种方法二分搜索，先从左右两端找到非空字符串的位置，然后如果运气好，碰到中间为非空比较大小，缩小范围；如果中间恰好是个非空字符串，则
往前（或往后）找到非空字符，比较，再缩小范围。【个人觉得不是专门搞算法的，这个题没必要在那点时间复杂度上较劲】
'''