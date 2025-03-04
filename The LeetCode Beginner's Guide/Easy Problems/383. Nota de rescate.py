"""
Given two strings ransomNote and magazine, return true if 
ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

args:
    ransomNote: str
    magazine: str
return:
    bool
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
        
        """dictionary = {}

        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        
        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False
        return True"""
        
        """magazine_counter = Counter(magazine)
        for char in ransomNote:
            if char not in magazine_counter or magazine_counter[char] == 0:
                return False
            magazine_counter[char] -= 1
        return True"""