class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 

        frequency_calc_s1 = {}
        frequency_calc_s2 = {}

        for i in range(len(s1)):

            if s1[i] not in frequency_calc_s1.keys():
                frequency_calc_s1[s1[i]] = 1
            else:
                frequency_calc_s1[s1[i]] += 1

            if s2[i] not in frequency_calc_s2.keys():
                frequency_calc_s2[s2[i]] = 1
            else:
                frequency_calc_s2[s2[i]] += 1

        while frequency_calc_s1:

            if next(iter(frequency_calc_s1)) != next(iter(frequency_calc_s2)):
                return False

            frequency_calc_s2.pop(next(iter(frequency_calc_s2)))
            frequency_calc_s1.pop(next(iter(frequency_calc_s1)))

        return True
