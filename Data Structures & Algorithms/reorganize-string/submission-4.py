class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        max_freq, max_cha = max((f, c) for c, f in count.items())

        print(max_freq, max_cha)
        # max_freq = 0
        # max_cha = ""
        # for cha, freq in count.items():
        #     if freq > max_freq:
        #         max_freq, max_cha = freq, cha
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [""] * len(s)
        order = [max_cha] + [key for key in count if key != max_cha]

        i = 0
        for cha in order:
            for _ in range(count[cha]):
                res[i] = cha
                i = i+2 if i+2 < len(s) else 1

        return "".join(res)
    
