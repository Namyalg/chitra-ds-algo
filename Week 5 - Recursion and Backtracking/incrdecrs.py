
def decrease(n):
    if n == 0:
        return
    print(n)
    decrease(n-1)
  
def increase(n):
    if n == 0:
        return 
    increase(n-1)
    print(n)

increase(4)
decrease(4)
