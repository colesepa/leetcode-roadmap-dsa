from typing import Any

class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self, item: Any) -> None:
        
        self.items.append(item)
    
    def pop(self) -> Any:
        
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self) -> Any:
        
        if self.is_empty():
            return None
         
        return self.items[len(self.items)-1]
    
    def is_empty(self) -> bool:
        
        if len(self.items) == 0:
            return True
        else:
            return False 
    
        
        