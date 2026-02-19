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
