class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       ''' my code starts from here: '''
       
        n = len(numbers)
        i = 0
        j = n-1
        while(i<j):
            if numbers[i] + numbers[j] == target:
                return (i+1, j+1)
            
            elif numbers[i] + numbers[j] > target:
                j = j-1
            
            elif numbers[i] + numbers[j] < target:
                i = i+1
