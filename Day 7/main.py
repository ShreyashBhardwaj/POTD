class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        first_occurrence = {0: -1}
        max_len = 0

        for i, val in enumerate(arr):
            if val > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                max_len = i + 1

            elif (prefix_sum - 1) in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len


sol = Solution()

print(sol.longestSubarray(arr = [1, 2, 3, 4, 1], k = 2))
print(sol.longestSubarray(arr = [6, 5, 3, 4], k = 2))
