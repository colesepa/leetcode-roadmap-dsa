# Reverse String With Stack

## Dificuldade
Easy

## Estrutura treinada
Stack

## Descrição
Dada uma string, retorne essa string invertida usando uma stack.

## Exemplos

Entrada:
"python"

Saída:
"nohtyp"

Entrada:
"abc"

Saída:
"cba"

Entrada:
""

Saída:
""

## Restrições
- Use uma lista como stack.
- Não use slicing `[::-1]`.
- Não use `reversed()`.

## Antes de resolver, pense:
- Como empilhar todos os caracteres?
- Como retirar os caracteres na ordem inversa?
- Como montar a string final?

## Hints

### Hint 1
Primeiro percorra a string e empilhe cada caractere.

### Hint 2
Depois desempilhe até a stack ficar vazia.

### Hint 3
Concatene os caracteres removidos em uma nova string.

### My Solution
```Python
def solution(word: str) -> str:
    
    stack = [] 
    reversed_stack = []
    for char in word:
       
       stack.append(char) 
   
    while stack:
        reversed_stack.append(stack.pop()) 
    
    return "".join(reversed_stack)
```

### Complexity
Temp -> O(n)
Space -> O(n)

## Observações:
Concatenação de strings usando +=, acarreta em maior cursto, uma vez que, para cada adição de caracter, a função deve
pecorrer a lista de strings e criar uma nova string. Esse fato se dá, devido a string ser imutável. Dessa forma, utilizar ".join" reduz o custo operacional, já que a função pecorre a lista um só vez pra criar uma úinica string.q