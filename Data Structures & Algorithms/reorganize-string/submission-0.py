class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        sort = sorted(count.items(), key=lambda x: x[1], reverse = True)
        res = [""] * len(s)

        max_cha, max_freq = sort[0]
        if max_freq > math.ceil(len(s) / 2):
            return ""

        i = 0
        for cha, freq in count.items():
            for _ in range(freq):
                if i >= len(s):
                    i = 1
                res[i] = cha
                i += 2

        return "".join(res)
    
