import re
class Solution:
    def detect_capital_use(self, word:str)-> bool:
        pattern = '[A-Z]'
        capital_count = len(re.findall(pattern, word))
        if capital_count == len(word):
            return True
        elif capital_count == 0:
            return True
        elif capital_count == 1 and word[0].isupper():
            return True
        else:
            return False