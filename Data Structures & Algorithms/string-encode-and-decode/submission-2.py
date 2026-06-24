class Solution:

    def encode(self, strs: List[str]) -> str:
        full = ""
        for s in strs:
            full = full + str(len(s)) + "#" + s
        return full


    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1 + length
            word = s[j+1:i]
            result.append(word)

        return result
        

