#2300. Successful Pairs of Spells and Potions


import bisect

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        res = []
        potions.sort()
        m = len(potions)
        for spell in spells:
            # threshold = (success+spell-1)//spell
            threshold = success/spell +1
            idx = bisect.bisect_left(potions,threshold)
            res.append(m-idx)
        return res
