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


