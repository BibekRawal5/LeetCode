
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 5000,
        'M': 1000
        }
        int_return = 0
        length = len(s)
        i = 0
        while i < length:
            char = s[i]
            power = length - i - 1
            if (char == 'I' or char == 'X' or char == 'C') and i != length - 1:
                if s[i+1] == 'V' or s[i+1] == 'L' or s[i+1] == 'D':
                    int_return += roman_dict[s[i+1]] - roman_dict[char]
                    i += 1
                    print("inside 1 if", int_return)
                elif s[i+1] == 'X' or s[i+1] == 'C' or s[i+1] == 'M':
                    int_return += roman_dict[s[i+1]] - roman_dict[char]
                    i += 1
                    print("inside 2 if", int_return)
                else:
                    int_return += roman_dict[char]
                    print("inside else", int_return)
            else:
                int_return += roman_dict[char]
                print("outside else",int_return)
            i += 1
            
        return int_return
            
                
            
