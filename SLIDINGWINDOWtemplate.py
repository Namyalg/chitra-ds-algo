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
