class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        ins_pos = 0

        for i in range(n):
            if arr[i] != 0:
                arr[ins_pos] = arr[i]
                ins_pos+=1

        for i in range(ins_pos,n):
            arr[i]=0
        return arr

sol = Solution()

print(sol.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))
print(sol.pushZerosToEnd([10, 20, 30]))
print(sol.pushZerosToEnd([0, 0]))
