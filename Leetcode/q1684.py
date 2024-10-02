from typing import Optional 

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowedStr = [x for x in allowed] # splits it into a list 
        a = 0 
        state = False # to check if there word contains the correct letters

        for word in words: #goes through all words in the list 
            for _ in word: #goes through all characters in the word
                if _ not in allowedStr: #if char is not permitted 
                    state = False # set state to false if it was previously set to true
                    break # breaks the loop as the str no longer is permitted 
                else: 
                    state = True #set state to true if char is permitted 
            
            if state == True: 
                a+=1 #inc count if the str is permitted 
                state = False #reset state for the next word 

        return a

