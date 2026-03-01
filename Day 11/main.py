class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr) -1
        m = n
        c=0
        while n !=0 :
            if arr[n]==0:
                arr.pop(n)
                c+=1
                n=len(arr)-1
            else:
                n-=1

        for i in range(c):
           arr.append(0)
        # ins_pos = 0
        # for i in range(n):
        #     if arr[i] != 0:
        #         arr[ins_pos] = arr[i]
        #         ins_pos+=1
        #
        # for i in range(ins_pos,n):
        #     arr[i]=0
        return arr

sol = Solution()

print(sol.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))
print(sol.pushZerosToEnd([10, 20, 30]))
print(sol.pushZerosToEnd([0, 0]))
