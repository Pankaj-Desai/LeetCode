# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

##SOLUTION##

class Solution:
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quicksort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quicksort(array, low, pi - 1)
            self.quicksort(array, pi + 1, high)
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        N = len(array)
        self.quicksort(array, 0, N - 1)
        if len(array) % 2 != 0:
            return array[int(len(array)/2)]
        else:
            return (array[int(len(array)/2)-1] + array[int(len(array)/2)]) / 2