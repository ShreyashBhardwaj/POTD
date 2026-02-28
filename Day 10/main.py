
class Solution:
    def findClosestPair(self,arr1, arr2, x):
        n = len(arr1)
        m = len(arr2)

        i = 0
        j = m - 1

        min_diff = float('inf')
        best_pair = None

        while i < n and j >= 0:
            current_sum = arr1[i] + arr2[j]
            current_diff = abs(current_sum - x)

            if current_diff < min_diff:
                min_diff = current_diff
                best_pair = (arr1[i], arr2[j])

            if current_sum > x:
                j -= 1
            elif current_sum < x:
                i += 1
            else:
                break  # Exact match found

        return best_pair


sol = Solution()
print(sol.findClosestPair(arr1=[1, 4, 5, 7], arr2=[10, 20, 30, 40], x=32))
print(sol.findClosestPair(arr1=[1, 4, 5, 7], arr2=[10, 20, 30, 40], x=50))
