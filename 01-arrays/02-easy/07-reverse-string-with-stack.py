def solution(word: str) -> str:
    
    stack = [] 
    reversed_stack = []
    for char in word:
       
       stack.append(char) 
   
    while stack:
        reversed_stack.append(stack.pop()) 
    
    return "".join(reversed_stack)

        