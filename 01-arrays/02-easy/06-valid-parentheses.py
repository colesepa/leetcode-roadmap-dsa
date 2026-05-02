def solution(text: str) -> bool:
   
    pair = {
        "(":")",
        "{":"}",
        "[":"]",
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    stack = []
    for char in text:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            if pair[char] != stack.pop():
                return False
    return len(stack) == 0
