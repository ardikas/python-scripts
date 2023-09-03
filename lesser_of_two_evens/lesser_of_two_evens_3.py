# Clean it up further, by simply just 'return'ing the results

def lesser_of_two_evens(a,b):
    
    if a % 2 == 0 and b % 2 == 0:
        # BOTH NUMBERS ARE EVEN!
        return min(a,b)
    else:
        # ONE OR BOTH NUMBERS ARE ODD!
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
