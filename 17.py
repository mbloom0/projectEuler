#Problem 17: Number letter counts
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

onesPlace = {
    "0":"",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

teensPlace = {
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen"
}

tensPlace = {
    "0":"",
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety"
}

#hundreds = {
    # just ones plus "hundred" i,e. one hundred, two hundred, eight hundred, nine hundred
#}

#thousands = {
    # just ones plus "thousand" i,e. one thousand, two thousand, eight thousand, nine thousand
#}

def numToEnglishString(num):
    """converts integer to english representation of the number as a string, works for numbers 1 to 9999"""
    numAsList = list(str(num)) # ['1','0','0']
    
    while len(numAsList) < 4:
        numAsList= ["0"] + numAsList

    def ones(numChar):
        return onesPlace.get(numChar)
    
    def lastTwo(numChars):
        numChars = list(numChars)
        """ 
        #TODO: replace the not zeroes with "X" and replace the if/else with a switch block; also for lastThree...
        switch = {
        
        elif numChars[0] == "1" and numChars[1] == "0":
            #ten
            return tensPlace.get(numChars[0])
        elif numChars[0] == "1" and numChars[1] != "0":
            #teens
            return teensPlace.get(''.join(numChars))
        elif numChars[0] != "1" and numChars[1] != "0":
            #tens-ones
            return tensPlace.get(numChars[0]) +"-"+ ones(numChars[-1])
        }
        if numChars[0] == "0":
            #ones
            return ones(numChars[-1]) 
        """
        if numChars[0] == "0":
            #ones
            return ones(numChars[-1])
        elif numChars[0] == "1" and numChars[1] == "0":
            #ten
            return tensPlace.get(numChars[0])
        elif numChars[0] == "1" and numChars[1] != "0":
            #teens
            return teensPlace.get(''.join(numChars))
        elif numChars[0] != "1" and numChars[1] != "0":
            #tens-ones
            return tensPlace.get(numChars[0]) +"-"+ ones(numChars[-1])
        else:
            #tens
            return tensPlace.get(numChars[0])

    def hundreds(numChar):
        if numChar != "0":
            return ones(numChar) + " hundred"
        else:
            return ""

    def lastThree(numChars):
        numChars = list(numChars)
        if numChars[0] == "0":
            #no hundreds
            return ""
        elif numChars[0] != "0" and numChars[1] == "0" and numChars[2] == "0":
            #hundred (only)
            return hundreds(numChars[0])
        else:
            #hundreds and somthing
            return hundreds(numChars[0]) + " and "


    def thousands(numChar):
        #TODO: replace with "lastFour" method which would consider when to put "and" or spaces.
        if numChar != "0":
            return ones(numChar) + " thousand "
        else:
            return ""

    numInEnglish = ""
    for i in range(3):
        switch = {
            0:thousands(numAsList[i]),
            1:lastThree(numAsList[1:4]),
            2:lastTwo(numAsList[2:4])
        }
        numInEnglish = numInEnglish + switch.get(i)
    
    return numInEnglish

englishFirstThousandNums = []
for i in range(1,1001):
    englishFirstThousandNums.append(numToEnglishString(i))

sampleOfOutput = englishFirstThousandNums[1:223]+englishFirstThousandNums[-223:-1]
sampleOfOutput.append(englishFirstThousandNums[len(englishFirstThousandNums)-1]) #1000

print("First Thousand numbers in english: " + str(sampleOfOutput) )

def countCharacters(word):
    length = 0
    for char in word:
        if char != ' ' and char != '-': length += 1
    return length

print("Sum of lengths of words in first thousand numbers: " + str(sum(list(map(countCharacters,englishFirstThousandNums)))))