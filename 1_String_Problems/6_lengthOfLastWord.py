# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

def lengthOfLastWord(s):
    words = s.strip().split()
    
    if not words:
        return 0
    
    return len(words[-1])