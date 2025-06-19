class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      if not nums:
        return 0

      #Use a Hash Set
      num_set = set(nums) # O(n)
      output = 0

      for num in num_set:
        #if num-1 is not in the set, count that
        if num-1 not in num_set:
            length = 1
            #keep walking as far as you can
            while num +length in num_set:
                length += 1
            output = max(output, length)

      return output
