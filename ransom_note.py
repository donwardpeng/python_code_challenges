'''
Easy: Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"

Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"

Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"

Output: true

 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution:
    def compare(self, ransom_note, magazine):
        for letter in ransom_note:
            if (letter in magazine):
                index_of_letter = magazine.index(letter)
                magazine = magazine[:index_of_letter:] + magazine[index_of_letter+1::]
            else:
                return False
        return True


if __name__ == "__main__": 
    solution = Solution()
    print('Input: ransomNote = "a", magazine = "b"')
    result = solution.compare('a', 'b')
    print(f'Output: {result}')

    print('Input: ransomNote = "aa", magazine = "ab"')
    result = solution.compare('aa', 'ab')
    print(f'Output: {result}')

    print('Input: ransomNote = "aa", magazine = "aab"')
    result = solution.compare('aa', 'aab')
    print(f'Output: {result}')

    print('Input: ransomNote = "you must pay", magazine = "you mst pay"')
    result = solution.compare('you must pay', 'you mst pay')
    print(f'Output: {result}')

    print('Input: ransomNote = "you must pay", magazine = "you must pay now"')
    result = solution.compare('you must pay', 'you must pay now')
    print(f'Output: {result}')
