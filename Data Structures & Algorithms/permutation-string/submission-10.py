class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False

        count, want = {}, {}
        # 1. Initialize the first window
        for i in range(m):
            want[s1[i]] = want.get(s1[i], 0) + 1
            count[s2[i]] = count.get(s2[i], 0) + 1

        # 2. Slide through the rest of the string
        # We use n - m to ensure we have room to add s2[i + m]
        for i in range(n - m):
            if count == want:
                return True
            
            # Update the sliding window: Remove Left
            left_char = s2[i]
            count[left_char] -= 1
            if count[left_char] == 0:
                del count[left_char]
            
            # Update the sliding window: Add Right
            right_char = s2[i + m]
            count[right_char] = count.get(right_char, 0) + 1

        # 3. CRITICAL: Check the very last window after the loop finishes
        return count == want