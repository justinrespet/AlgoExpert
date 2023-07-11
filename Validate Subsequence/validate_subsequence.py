"""
Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the
second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the
array but that are in the same order as they appear in the array. For instance, the 
numbers [1,2,4] form a subsequence of the array [1,2,3,4], and so do the numbers [2,4].
Note that a single number in an array and the array itself are both valid subsequences
of the array.
"""

# Sample Input
sampleArray = [5,1,22,25,6,-1,8,10]
sampleSequence = [1,6,8,10]

# To solve this problem:
def isValidSubsequence(array, sequence):
# 1. Create an index counter for subsequence
    index = 0
# 2. Iterate through supersequence
    for item in array:
# 3. If indexed element of subsequence is found in supersequence, increment index
        if sequence[index] == item:
            index += 1
# 4. If index equals length of subsequence, all elements in subsequence were found
#    in order, return true. Else, return false.
        if index == len(sequence):
            return True
    return False

print(isValidSubsequence(sampleArray, sampleSequence))

"""
Hint1: You can solve this question by iterating through the main input array once.

Hint2: Iterate through the main array, and look for the first integer in the potential
subsequence. If you find that integer, keep on iterating through the main array, but
now look for the second integer in the potential subsequence. Continue this process
until you either find every integer in the potential subsequence or you reach the end 
of the main array.

Hint3: To actually implement what Hint #2 describes, you'll have to declare a variable
holding your position in the potential subsequence. At first, this position, will be 
the 0th index in the sequence; as you find the sequence's integers in the main array,
you'll increment the position variable until you reach the end of the sequence.

Optimal Space & Time Complexity:
O(n) time | O(1) space
"""