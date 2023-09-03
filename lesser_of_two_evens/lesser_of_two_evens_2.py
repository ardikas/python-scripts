# Clean it up by using min(a,b) or max(a,b) functions - returns the min/max of the two numbers you're comparing

def lesser_of_two_evens(a,b):
    
    if a % 2 == 0 and b % 2 == 0:
        # BOTH NUMBERS ARE EVEN!
        result = min(a,b)
    else:
        # ONE OR BOTH NUMBERS ARE ODD!
        result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
