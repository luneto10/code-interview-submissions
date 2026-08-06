from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        if len(counter_s) != len(counter_t):
            return False
    
        for k, v in counter_s.items():
            value_t = counter_t.get(k, 0)
            if v != value_t:
                return False

        return True
