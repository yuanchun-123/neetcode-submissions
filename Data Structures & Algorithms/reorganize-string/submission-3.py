class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_freq = 0
        max_cha = ""
        for cha, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                max_cha = cha

        res = [""] * len(s)
        if max_freq > math.ceil(len(s) / 2):
            return ""

        order = [max_cha]
        for cha, freq in count.items():
            if cha == max_cha:
                continue
            order.append(cha)

        i = 0
        for cha in order:
            for _ in range(count[cha]):
                if i >= len(s):
                    i = 1
                res[i] = cha
                i += 2

        return "".join(res)
    
