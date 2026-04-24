class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        '''My code starts from here : '''
        
        i = 0
        j = 1
        uniq = 1
        n = len(nums)
        while(j<n):
            if nums[j] == nums[j-1]:
                j = j+1
                continue
            
            nums[i+1] = nums[j]
            i = i+1
            uniq = uniq+1
            j = j+1

        return uniq