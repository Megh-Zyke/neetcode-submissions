class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {} 

        for letter in s: 
            if letter not in counts: 
                counts[letter] = 0 
            counts[letter] += 1
        
        for letter in t: 
            if letter in counts:
                counts[letter]-=1
            else:
                return False
        
        for i in counts:
            if counts[i] != 0: 
                return False
        return True