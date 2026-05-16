# Valid Palindrome

## Dificuldade
Easy

## Estrutura treinada
String

## Padrão
Two Pointers

## Descrição
Dada uma string, determine se ela é um palíndromo.

Um palíndromo é uma palavra ou frase que permanece igual quando lida de trás para frente.

Ignore:
- espaços
- pontuação
- diferenças entre maiúsculas e minúsculas

## Exemplos

Entrada:
"A man, a plan, a canal: Panama"

Saída:
True

---

Entrada:
"race a car"

Saída:
False

---

Entrada:
" "

Saída:
True

## Restrições
- Não use `[::-1]`.
- Não use `reversed()`.
- Ignore caracteres não alfanuméricos.
- Ignore diferenças entre maiúsculas e minúsculas.

## Antes de resolver, pense:
- Como comparar início e fim ao mesmo tempo?
- Como ignorar caracteres inválidos?
- O que fazer quando encontrar espaços ou pontuação?

## Hints

### Hint 1
Use dois ponteiros:
- um no início
- um no final

### Hint 2
Avance os ponteiros até encontrar caracteres válidos.

### Hint 3
Compare os caracteres em lowercase.

## Sua solução
```python
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
```
def solution(text: str) -> bool:
## Solução sugerida
```python
    i = 0
    j = len(text) - 1

    while i < j:
        while i < j and not text[i].isalnum():
            i += 1

        while i < j and not text[j].isalnum():
            j -= 1

        if text[i].lower() != text[j].lower():
            return False

        i += 1
        j -= 1

    return True
```

## Análise
Complexidade de tempo: O(n)
Complexidade de espaço: O(n)

## Revisão

Minha solução, apesar de apresentar o resultado esperado, porém pode
apresentar falha, quando as strings passadas forem só acentos. 

A verificação de char alfa-numérico pode quebrar se não colocarmos limites
nos ponteiros. Dessa forma, a verificação deve se limitar até o índece
do ponteiro "j".  
