"""
Given an array arr[] of integers and a range [low, high], find all the numbers within the range that are not present in the array. return the missing numbers in sorted order.

Examples:

Input: arr[] = [10, 12, 11, 15], low = 10, high = 15
Output: [13, 14]
Explaination: Numbers 13 and 14 lie in the range [10, 15] but are not present in the array.
Input: arr[] = [1, 4, 11, 51, 15], low = 50, high = 55
Output: [50, 52, 53, 54, 55]
Explaination: Numbers 50, 52, 53, 54 and 55 lie in the range [50, 55] but are not present in the array.



"""


class Solution:
    def missingRange(self, arr, low, high):
        # code here
        missing_arr = []
        l_h_range = range(low, high + 1)
        # arr.sort()
        myset = set(arr)

        for i in l_h_range:
            if i not in myset:
                missing_arr.append(i)

        return missing_arr
