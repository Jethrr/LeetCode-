class Solution:
    def isPalindrome(self, s: str) -> bool:
                return (newStr := ''.join(char.lower() for char in s if char.isalnum())) == newStr[::-1]
