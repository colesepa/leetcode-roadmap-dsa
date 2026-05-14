def my_solution (palindrome: str) -> bool:
    
    palindrome = palindrome.lower()

    i = 0
    j = len(palindrome) - 1
    if not len(palindrome.strip()):
        return True
    while i <= j:
        while not palindrome[i].isalnum():
            i += 1
        while not palindrome[j].isalnum():
            j -= 1
        
        if palindrome[i] != palindrome[j]:
            return False
        
        else:
            i +=1
            j -= 1
    return True
                    

print(my_solution("A man, a plan, a canal: Panama"))
print(my_solution(" "))
print(my_solution("race a car"))

def solution(word: str) -> bool:
    i = 0
    j = len(word) - 1  

    while i < j: # Limitador dos ponteiros
        
        # Verificação se os chars são números ou letras e se estão dentro do limite da string
        while i < j and not word[i].isalnum():
            i += 1
        while i < j and not word[j].isalnum():
            j -= 1
        
        # Verificação se os char's são diferentes
        if word[i].lower() != word[j].lower():
            return False
        else:
            i +=1
            j -= 1
    return True

print(solution("A man, a plan, a canal: Panama"))
print(solution(" "))
print(solution("race a car"))