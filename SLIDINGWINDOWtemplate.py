        #start is i
        #end is j
        #definite window size is k
        
        For a fixed window this is the main pproach
        For subarray and substring questions
        O(n) approach is given by this method
        
        i = 0
        j = 0
        k = 3
        
        s = 0
        
        #while end is less than length
        
        while j < len(a):
                
            #do some operation
        
            s += a[j]
            
        #if size of window is smaller then keep incrementing j
                if j - i + 1 < k:
                j += 1
              
        #else if the window of desired size is found, then increment i as well
        
            elif j - i + 1 == k:
                print("sum is ", s)
                
                #obtain the result from the window and then move to the next window
                
                #often queues can be used with sliding window as it follows the FIFO policy
                s = s - a[i]
                i += 1
                j += 1

                
               _________________________________________
        #very slow but still passes, this is brute force, get the window and then sort and return mid

#more optimised solutin using heap canbe dpne
#this is the brute force for finding median
O(n*nlogn)

#better thn brute force
#which is O(n*n*n*logn)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        i = 0
        j = 0
        mdns = []
        while j < len(nums):
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                f = sorted(nums[i : j+1])
                if len(f) & 1:
                    mdns.append(f[len(f)//2])
                else:
                    m1 = f[len(f)//2]
                    m2 = f[len(f)//2 - 1]
                    mdns.append((m1+m2)/2)
                i += 1
                j += 1
        return mdns

______________________________________________________________________________________
#Variable sliding window

#Here u have to satisfy the condition, nt based on the window size

start = 0
end = 0



while end < len(nums):
        if < condiion:
                end += 1
        if  === condition:
                store the result
                end += 1
        if > conditin:
                while condition > k:
                        compute the condition
                        strt += 1  
                end += 1


                
                
                
     SLIDING WINDOW IS ALSO CLOSELY RELATED TO PREFIX SUM AND HASHMAP, IT IS AN ALTERNATIVE TO THIS APPROACH

#in this sliding window problem WHEN DOING PREFIX SUM ALWAYS ADD SUM OF 0 in the beginning

#as if the sum of the first few elements itself is the target it wont be accountted for

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        sums = dict({0: 1})
        prf = 0
        cnt = 0
        
        USING A FOR LOOP
        
        for i in range(len(A)):
            prf += A[i]
            if prf - S in sums:
                cnt += sums[prf - S]
            if prf not in sums:
                sums[prf] = 0
            
    

VARIABLE SIZE WINDOW

     
        
        left = 0
        s = 0
        res = float('inf')
        
        KEEP INCREMENTING TAIL PTR AND WHEN CONDITION IS VIOLATED MOVE THE HEAD
        
        RUNS IN o(N) TIME AND HAS A SPACE OF o(1)
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                res = min(res, i + 1 - left)
                s -= nums[left]
                left += 1
        return 0 if res == float('inf') else res'''
        
        s = 0
        j = 0
        i = 0
        res = float('inf')
        while i < len(nums):
            s += nums[i]
            while s >= target:
                res = min(res, i + 1 - j)
                s -= nums[j]
                j += 1 
            i += 1
        return 0 if res == float('inf') else res
        
        
        
          
            sums[prf] += 1
        return cnt
