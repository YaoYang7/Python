class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
        ans = 0
        i = 0
        
        # Loop through the entire string
        while i < len(s):
            # Check if the current numeral is less than the next numeral
            if i+1 < len(s) and romanDict[s[i]] < romanDict[s[i+1]]:
                # If it is, this means we have a subtractive combination
                # For example, "IV" or "IX"
                # Add the value of the next numeral and subtract the value of the current numeral
                ans += romanDict[s[i+1]] - romanDict[s[i]]
                # Move index forward by 2 as 2 chars have processed 
                i += 2
            else:
                # If the current numeral is not less than the next numeral
                # or there is no next numeral, just add the value of the current numeral
                ans += romanDict[s[i]]
                # Move index forward by 1 as 1 char has passed
                i += 1
        return ans


if __name__ == "__main__":
    s = Solution() 
    t = "MCMXCIV"

    print(s.romanToInt(t)) # 1994