class Solution:
    def longestSubarray(self, arr, k):

        low =[]
        high =[]
        answer = 0
        for i,element in enumerate(arr):
            if element <= k:
                low.append(element)
            else:
                high.append(element)


            if len(high)>len(low):
                answer+=1


        return answer


sol = Solution()

print(sol.longestSubarray(arr = [1, 2, 3, 4, 1], k = 2))
print(sol.longestSubarray(arr = [6, 5, 3, 4], k = 2))
