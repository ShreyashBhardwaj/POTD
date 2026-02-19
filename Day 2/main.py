"""
Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

Examples:

Input: arr[] = [3, 30, 34, 5, 9]
Output: 9534330
Explanation: Given numbers are [3, 30, 34, 5, 9], the arrangement [9, 5, 34, 3, 30] gives the largest value.
Input: arr[] = [54, 546, 548, 60]
Output: 6054854654
Explanation: Given numbers are [54, 546, 548, 60], the arrangement [60, 548, 546, 54] gives the largest value.
Input: arr[] = [3, 4, 6, 5, 9]
Output: 96543
Explanation: Given numbers are [3, 4, 6, 5, 9], the arrangement [9, 6, 5, 4, 3] gives the largest value.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105


"""

class Solution:

    def findLargest(self, arr):
        # code here
        string_to_concat = ""
        proper_dict = self.getDictionary(arr)


        while proper_dict.keys():


            print(proper_dict)
            high = max(proper_dict.keys())

            if len(proper_dict[high]) == 1:
                string_to_concat = string_to_concat + "".join(map(str,proper_dict[high]))
            else:
                sorted_list = sorted(proper_dict[high], key= lambda x: str(x)*10, reverse=True)
                string_to_concat = string_to_concat + "".join(map(str,sorted_list))

            print(string_to_concat)
            proper_dict.pop(high)

        if string_to_concat.startswith("0"):
            string_to_concat=0
        print(string_to_concat)


    def singleDigitorMore(self, element):
        while (element != 0):
            if element // 10 == 0:
                return element
            else:
                element = element // 10
        return 0

    def getDictionary(self,arr):
        dictionary = {}
        for i in arr:
            element =  self.singleDigitorMore(i)

            if element in dictionary.keys():
                dictionary[element].append(i)
            else:
                dictionary[element] = [i]


        print(dictionary)
        return dictionary

sol = Solution()
# sol.findLargest([3, 30, 34, 5, 9])
# sol.findLargest([4, 5, 7, 15, 20, 11])
sol.findLargest([0,0,0,0,0,0])
