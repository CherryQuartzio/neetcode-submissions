class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in (s if len(s) > len(t) else t):
            char_count_s = s.count(char)
            char_count_t = t.count(char)

            if (char_count_s != char_count_t):
                return False
        return True
        