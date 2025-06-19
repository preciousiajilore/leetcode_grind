"""
DONT DO THIS LOL
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        for num in numbers:
            look = target - num
            if look in numbers:
                output.append(numbers.index(look) + 1)
        
        output.sort()
        return output
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #Use two pointers
       l , r = 0, len(numbers) - 1

       while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum == target:
            return [l+1, r+1]
        elif currSum > target:
            r -= 1
        else:
            l += 1
