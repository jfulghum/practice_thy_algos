class Solution:
    def romanToInt(self, s: str) -> int:
        common = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        special = {
            "IV": 2,
            "IX": 2,
            "XL": 20,
            "XC": 20,
            "CD": 200,
            "CM": 200,
        }
        result = 0
        for i in range(len(s)):
            result -= special.get(s[i:i+2],0)
            result += common.get(s[i],0)
        return result
