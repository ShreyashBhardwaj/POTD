"""
Given two binary arrays, a1[] and a2[] of equal length. Find the length of longest common span (i, j), where i<= j such that a1[i] + a1[i+1] + .... + a1[j] =  a2[i] + a2[i+1] + ... + a2[j].

Examples:

Input: a1[] = [0, 1, 0, 0, 0, 0], a2[] = [1, 0, 1, 0, 0, 1]
Output: 4
Explanation: The longest span with same sum is from index 1 to 4 (0-based indexing).
Input: a1[] = [0, 1, 0, 1, 1, 1, 1], a2[] = [1, 1, 1, 1, 1, 0, 1]
Output: 6
Explanation: The longest span with same sum is from index 1 to 6 (0-based indexing).
Input: a1[] = [0, 0, 0], a2[] = [1, 1, 1]
Output: 0
Explanation: There is no span where the sum of the elements in a1[] and a2[] is equal.


"""


class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        length = len(a1)
        span_length = 0
        max_len = 0
        prev_sum_a1, prev_sum_a2, current_diff = 0, 0, 0
        diff_map = {0: -1}
        for i in range(length):
            prev_sum_a1 = prev_sum_a1 + a1[i]
            prev_sum_a2 = prev_sum_a2 + a2[i]

            current_diff = prev_sum_a1 - prev_sum_a2

            if current_diff in diff_map:
                span_length = i - diff_map[current_diff]
                max_len = max(max_len, span_length)
            else:
                diff_map[current_diff] = i

        return max_len


sol = Solution()
print(sol.equalSumSpan([0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]))  # 4
print(sol.equalSumSpan([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]))  # 6
print(sol.equalSumSpan([0, 0, 0], [1, 1, 1]))  # 0
