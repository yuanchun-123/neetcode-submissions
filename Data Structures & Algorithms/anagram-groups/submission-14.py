class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapping = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            mapping[tuple(count)] = mapping.get(tuple(count), []) + [s]
        
        for key, value in mapping.items():
            res.append(list(value))
        return res
                


