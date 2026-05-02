from typing import Any

class MinStack:
    
    def __init__(self) -> None:
        
        self.items = []
        self.ordered_items = []

        
    def is_empty(self) -> bool:
        
        if len(self.items) == 0:
            return True
        
        return False
    
    def push(self, value: int) -> None:
        self.items.append(value)
        if len(self.ordered_items) == 0 or value <= self.ordered_items[-1]:
            self.ordered_items.append(value)

        
    
    def pop(self) -> Any:
        
        if self.is_empty():
            return None

        value = self.items.pop()

        if value == self.ordered_items[-1]:
            self.ordered_items.pop()
        
        return value

    def peek(self) -> Any:
        
        if self.is_empty():
            return None
            
        return self.items[len(self.items)-1]

    def get_min(self) -> Any:
        
        if len(self.ordered_items) == 0:
            return None
        
        return self.ordered_items[-1]

