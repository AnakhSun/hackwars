'''
You will be given an array of numbers which represent your character's altitude above sea level at regular intervals:

Positive numbers represent height above the water.
0 is sea level.
Negative numbers represent depth below the water's surface.
Create a function which returns whether your character survives their unsupervised diving experience, given an array of integers.

Your character starts with a breath meter of 10, which is the maximum. When diving underwater, your breath meter decreases by 2 per item in the array. Watch out! If your breath diminishes to 0, your character dies!

To prevent this, you can replenish your breath by 4 (up to the maximum of 10) for each item in the array where you are at or above sea level.

Your function should return True if your character survives, and False if not.

[-5, -15, -4, 0, 5] ➞ True

// Breath meter starts at 10.
// -5 is below water, so breath meter decreases to 8.
// -15 is below water, so breath meter decreases to 6.
// -4 is below water, so breath meter decreases to 4.
// 0 is at sea level, so breath meter increases to 8.
// 5 is above sea level and breath meter is capped at 10 (would've been 12 otherwise).
// Character survives!
'''
def diving_minigame(array):
    oxygen = 10
    for pos in array:
        if pos >= 0:
            oxygen += 4
            if oxygen > 10:
                oxygen = 10
        if pos <= 0:
            oxygen -= 2
        if oxygen <= 0:
            return False
    
    return oxygen>0
    
    
print(diving_minigame([0, -4, 0, -4, -5, -2]))

