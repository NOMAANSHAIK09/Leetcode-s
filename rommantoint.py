class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(s)):
            print(s[i+1])
            # If current value < next value → subtract it
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total


# --- main part ---
s = input("Enter a Roman numeral: ")   # Example: XIV
solution = Solution()
result = solution.romanToInt(s)
print("Integer value:", result)
