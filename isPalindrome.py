class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered =[]
        for char in s :
            if char.isalnum():
                filtered.append(char.lower())
        
        filtString = "".join(filtered)
        return filtString == filtString[::-1]
