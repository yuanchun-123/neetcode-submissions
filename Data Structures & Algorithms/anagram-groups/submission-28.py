class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for cha in s:
                count[ord(cha)-ord('a')] += 1
            mapp[tuple(count)].append(s)
        return list(mapp.values())

