class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset=set(nums)

        for num in numset:
            if (num - 1) not in numset:
                i = 0
                while (num + i) in numset:
                    i += 1
                longest = max(longest, i)
        return longest