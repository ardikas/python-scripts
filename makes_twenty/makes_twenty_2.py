# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# To make it super clean, you can put all of this in a single line, using 'return' and 'or'

def makes_twenty(n1,n2):

    return (n1+n2) == 20 or n1 == 20 or n2 == 20

    pass



print(makes_twenty(20,10))
print(makes_twenty(2,3))
