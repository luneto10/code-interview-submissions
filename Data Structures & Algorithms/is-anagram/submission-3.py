class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_letter_dict = Counter(s)
        t_letter_dict = Counter(t)

        for k, v in s_letter_dict.items():
            t_value = t_letter_dict.get(k)
            if not t_value or t_value != v:
                return False
        return True
            
