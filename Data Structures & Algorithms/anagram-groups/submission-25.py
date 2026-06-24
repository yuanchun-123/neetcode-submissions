class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapp = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            mapp[tuple(count)].append(s)

        for key in mapp:
            cur = []
            for string in mapp[key]:
                cur.append(string)
            res.append(cur)
        
        return res

