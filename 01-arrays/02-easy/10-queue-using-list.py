from typing import Any

class Queue:
    
    def __init__(self) -> None:
        self.items = []


    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def peek(self) -> Any:
        
        if self.is_empty():
            return None
        
        return self.items[0]
        
    def enqueue(self, value: Any) -> None:
        self.items.append(value)
        
    def dequeue(self) -> Any:
            
        if self.is_empty():
            return None
        
        value = self.items[0]
        self.items.pop(0)
        
        return value