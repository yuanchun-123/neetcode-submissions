class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            mapping[tuple(count)].append(s)
        
        for key, value in mapping.items():
            res.append(list(value))
        return res
                


