        #start is i
        #end is j
        #definite window size is k
        
        For subarray and substring questions
        O(n) approach is given by this method
        
        i = 0
        j = 0
        k = 3
        
        s = 0
        while j < len(a):
            s += a[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                print("sum is ", s)
                s = s - a[i]
                i += 1
                j += 1
