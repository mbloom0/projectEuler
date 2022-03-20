#Problem 9: Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#To find a b and c we need to find all sets of a b c where a < b and b < c, and a+b+c = 1000, then filter for the one that is a pythagorean triplet (a^2 + b^2 = c^2)

def pythagoreanTriplet(triplet):
    """ Checks if a triplet (a,b,c) obeys pythagorean theorem"""
    a,b,c = triplet[0],triplet[1],triplet[2]
    if (a < b) and (b < c) and (a**2 + b**2 == c**2):
        return True
    else:
        return False

possibleTriplets = []

for c in range(3,998):
    for b in range(1,c):
        for a in range(1,b):
            if a+b+c == 1000: possibleTriplets.append((a,b,c))
print("Pythagorean triplet for which a+b+c = 1000: " +      str(list(filter(pythagoreanTriplet,possibleTriplets))))
