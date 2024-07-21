class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for elem in nums:
            if nums:
                if elem in hashset:
                    return True
                hashset.add(elem)
        return False