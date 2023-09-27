def is_balanced(expr):
    stack = []
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    
    for char in expr:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or opening.index(stack.pop()) != closing.index(char):
                return False

    return len(stack) == 0

# Test cases
print(is_balanced("(1 + 2) * {[(3 / 4) - 5]}")) # True
print(is_balanced("[1 + 2) * (3 - 4)]")) # False
print(is_balanced("((1 + 2)")) # False