class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        medi = len(nums1)//2
        if len(nums1)%2==1:
            return nums1[medi]
        else:
            return (nums1[medi]+nums1[medi-1])/2.0
