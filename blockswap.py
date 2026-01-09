l = [1,2,3,4,5,6,7,8,9,10]
target = 6
def two_sum(l):
    
    for i in l:
        if (target-i) in l and target != (target-i):
            return (i, target-i)
