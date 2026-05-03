from typing import Any

def solution(text: str) -> str | None:
    
    count: dict[str, int] = {}
    if not text:
            return None

    for char in text:
        count[char] = count.get(char, 0) + 1

    for char in text:
        if count[char] == 1:
            return char
    
    return None