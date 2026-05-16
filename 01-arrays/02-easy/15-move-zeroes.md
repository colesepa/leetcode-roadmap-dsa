# Move Zeroes

## Dificuldade
Easy

## Estrutura treinada
Array

## Padrão
Two Pointers

## Descrição
Dada uma lista de inteiros, mova todos os zeros para o final, mantendo a ordem relativa dos elementos não-zero.

A modificação deve ser feita na própria lista.

## Exemplos

Entrada:
[0, 1, 0, 3, 12]

Saída:
[1, 3, 12, 0, 0]

Entrada:
[0, 0, 1]

Saída:
[1, 0, 0]

## Restrições
- Não crie uma nova lista final.
- Modifique a lista original.
- Mantenha a ordem dos elementos não-zero.
- Não use `sort()`.

## Antes de resolver, pense:
- Como identificar a posição onde o próximo número não-zero deve ficar?
- Preciso mover os zeros ou mover os não-zeros?
- Como usar dois ponteiros?

## Hints

### Hint 1
Use um ponteiro para marcar onde colocar o próximo valor diferente de zero.

### Hint 2
Percorra a lista procurando valores não-zero.

### Hint 3
Depois de mover os não-zeros para frente, preencha o restante com zeros.

## Sua solução
```python

def my_solution(enum: list[int]) -> list[int]:

    i = 0
    while i < len(enum)-2:
        j = i+1
        if enum[i] == 0 and j <= len(enum)-1:
            while enum[j] == 0:
                j += 1
            enum[i] = enum[j]
            enum[j] = 0
        i += 1

    return enum
```

## solução sugerida
```python
def solution(enum: list[int]) -> list[int]:
    position = 0

    # Percorre a lista
    for i in range(0, len(enum)):

      # Avança o valor de posição até o valor de contagem de números não-zeros
        if enum[i] != 0:
            enum[position] = enum[i]
            position += 1
    while position < len(enum):
        enum[position] = 0
        position += 1

    return enum
```

## Análise
Complexidade de tempo da minha solução = O(n²)
Complexidade de tempo da solução sugerida = O(n)

## Revisão

Para a minha solução adotei uma solução de complexidade pior do que a solução sugrida, uam vez que,
minha soluçcão pecorre quase que na totalidade a lista mais de uma vez, verificando sempre o valor
atual e buscando o próximo valor para fazer a substituição. Por sua vez, a soluçcão sugerida 
apresenta uma solução que cria um ponteiro, que só é movimentado quando encontra um valor não nulo,
marcando a ultima posição de um valor não nulo e que por fim, preenche com o valor zero desde a
ultima posição armazena com valor não nulo até o final da lista.

