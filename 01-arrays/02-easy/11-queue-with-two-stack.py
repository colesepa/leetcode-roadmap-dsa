from typing import Any

class Queue:
    
    def __init__(self) -> None:
        self.input_stack = []
        self.output_stack = []

    
    def is_empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def enqueeu(self, value: Any) -> None:
        self.input_stack.append(value)
    
    def _transfer(self) -> None:
        
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())     
        
    def peek(self) -> Any:
        
        if self.is_empty():
            return None
        
        if not self.output_stack:
            self._transfer()
        
        return self.output_stack[-1]
    
    def dequeue(self) -> Any|None:
        
        if self.is_empty():
            return None
        
        if not self.output_stack:
            self._transfer()

        return self.output_stack.pop()