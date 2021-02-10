class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
        
        
      Logic is as follows
      
      
      Considering the array  => [5,3,2,1,6]
      
      A DP array   [1,1,1,1,1] is begun with as the minimum length of the increasing subsequence is 1, i.e just one element
      ______________________________________
      First iteration
      
      [5, 3, 2, 1, 6]
      
      [1, 1, 1, 1, 1] ==> [1, 1, 1, 1, 1] as 3 is lesser than 5
      
       j  i
      
      _________________________________
      Second iteration
      
         [5, 3, 2, 1, 6]
      
      1) [1, 1, 1, 1, 1] =>  [1, 1, 1, 1, 1] No change as 2 is lesser than 5  
      
          j     i
       
       
       2) [1, 1, 1, 1, 1] => [1, 1, 1, 1, 1] No change again as 2 is lesser than 3
       
             j   i
             
       ______________________________________________________
       
       Third iteration
       
       [5, 3, 2, 1, 6]
       
        j        i
        
        Same steps are followed here, and the result is [1, 1, 1, 1, 1] as no number is less than 1
        ________________________________________________________________________
        
        Fourth iteration
        
        [5, 3, 2, 1, 6]
        
         j           i
         
      1)[1, 1, 1, 1, 1]  Now the value of 5 is less than 6 so it is updated to  [1, 1, 1, 1, 2]
                                                                    
                    Max of itself and the position where it is greater
                    The underlying formula is dp[i] = max(dp[i], dp[j] + 1)
     
      2)Now the value of 3 is compared to 6, though it is (6) greater than 3, the value 3 is less than 5 so it cannot be a continouus sequence
      
      Thus the value of 6 is bounded to 2 applying the formula
      
      
      dp[i] = max(dp[i], dp[j] + 1)
          
         
