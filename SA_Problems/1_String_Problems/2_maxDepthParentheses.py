def maxDepthParentheses(s):
    depth = 0
    count = 0

    for i in s:
        if i == '(':
            depth += 1
            count = max(count, depth)
        elif i == ')':
            depth -= 1
    
    return count

max = maxDepthParentheses("(1+(2*3)+((8)/4))+1")
print(max)