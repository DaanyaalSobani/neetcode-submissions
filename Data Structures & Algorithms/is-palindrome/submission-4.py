class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(char.lower() for char in s if char.isalnum())
        print(reversed(new_str))
        print((new_str))
        return new_str == "".join(reversed(new_str))