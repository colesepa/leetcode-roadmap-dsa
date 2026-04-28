# Exercícios de Arrays/Listas — Estilo LeetCode

> Objetivo: praticar manipulação de arrays usando listas Python, com foco em raciocínio algorítmico.
>
> Regra geral: resolva usando funções. Não crie uma classe `Array`.
>
> Em vários exercícios, evite métodos prontos quando indicado, para treinar a lógica manual.

---

## 01. Buscar Índice de um Valor

**Dificuldade:** Fácil  
**Tópicos:** Array, busca linear

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `target`, retorne o índice da primeira ocorrência de `target` em `nums`.

Se `target` não existir na lista, retorne `-1`.

### Assinatura

```python
def solution(nums: list[int], target: int) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [10, 20, 30, 40], target = 30
Saída: 2
```

### Exemplo 2

```text
Entrada: nums = [5, 8, 12], target = 7
Saída: -1
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
```

### Observação

Não use `.index()`.

---

## 02. Contém Valor

**Dificuldade:** Fácil  
**Tópicos:** Array, busca linear, booleanos

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `target`, retorne `True` se `target` estiver presente na lista. Caso contrário, retorne `False`.

### Assinatura

```python
def solution(nums: list[int], target: int) -> bool:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4], target = 3
Saída: True
```

### Exemplo 2

```text
Entrada: nums = [1, 2, 3, 4], target = 9
Saída: False
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use o operador `in`.

---

## 03. Contar Ocorrências

**Dificuldade:** Fácil  
**Tópicos:** Array, contagem

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `target`, retorne quantas vezes `target` aparece na lista.

### Assinatura

```python
def solution(nums: list[int], target: int) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 2, 3, 2], target = 2
Saída: 3
```

### Exemplo 2

```text
Entrada: nums = [5, 5, 5], target = 1
Saída: 0
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `.count()`.

---

## 04. Maior Valor

**Dificuldade:** Fácil  
**Tópicos:** Array, comparação

### Enunciado

Dada uma lista não vazia de inteiros `nums`, retorne o maior valor presente na lista.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [4, 10, 2, 8]
Saída: 10
```

### Exemplo 2

```text
Entrada: nums = [-5, -2, -10]
Saída: -2
```

### Restrições

```text
1 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `max()`.

---

## 05. Menor Valor

**Dificuldade:** Fácil  
**Tópicos:** Array, comparação

### Enunciado

Dada uma lista não vazia de inteiros `nums`, retorne o menor valor presente na lista.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [4, 10, 2, 8]
Saída: 2
```

### Exemplo 2

```text
Entrada: nums = [-5, -2, -10]
Saída: -10
```

### Restrições

```text
1 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `min()`.

---

## 06. Soma dos Elementos

**Dificuldade:** Fácil  
**Tópicos:** Array, acumulador

### Enunciado

Dada uma lista de inteiros `nums`, retorne a soma de todos os seus elementos.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4]
Saída: 10
```

### Exemplo 2

```text
Entrada: nums = []
Saída: 0
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `sum()`.

---

## 07. Média dos Elementos

**Dificuldade:** Fácil  
**Tópicos:** Array, acumulador, divisão

### Enunciado

Dada uma lista não vazia de inteiros `nums`, retorne a média aritmética dos elementos.

### Assinatura

```python
def solution(nums: list[int]) -> float:
    pass
```

### Exemplo 1

```text
Entrada: nums = [10, 20, 30]
Saída: 20.0
```

### Exemplo 2

```text
Entrada: nums = [1, 2]
Saída: 1.5
```

### Restrições

```text
1 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `sum()`.

---

## 08. Inverter Lista

**Dificuldade:** Fácil  
**Tópicos:** Array, dois ponteiros

### Enunciado

Dada uma lista de inteiros `nums`, retorne uma nova lista com os elementos em ordem inversa.

### Assinatura

```python
def solution(nums: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3]
Saída: [3, 2, 1]
```

### Exemplo 2

```text
Entrada: nums = []
Saída: []
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não use `[::-1]`, `.reverse()` ou `reversed()`.

---

## 09. Inverter Lista In-Place

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, dois ponteiros, in-place

### Enunciado

Dada uma lista de inteiros `nums`, inverta seus elementos no próprio array e retorne a lista modificada.

### Assinatura

```python
def solution(nums: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4]
Saída: [4, 3, 2, 1]
```

### Exemplo 2

```text
Entrada: nums = [7]
Saída: [7]
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Não crie uma segunda lista. Use troca de posições.

---

## 10. Remover Valor

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, dois ponteiros, in-place

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `val`, remova todas as ocorrências de `val` da lista.

A ordem dos elementos restantes deve ser preservada.

Retorne uma nova lista contendo apenas os elementos diferentes de `val`.

### Assinatura

```python
def solution(nums: list[int], val: int) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [3, 2, 2, 3], val = 3
Saída: [2, 2]
```

### Exemplo 2

```text
Entrada: nums = [1, 2, 3, 4], val = 5
Saída: [1, 2, 3, 4]
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

---

## 11. Remover Valor In-Place

**Dificuldade:** Média  
**Tópicos:** Array, dois ponteiros, in-place

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `val`, remova todas as ocorrências de `val` modificando a lista original.

Retorne `k`, a quantidade de elementos restantes.

Após a execução, os primeiros `k` elementos de `nums` devem conter os valores diferentes de `val`.

A ordem dos elementos restantes deve ser preservada.

### Assinatura

```python
def solution(nums: list[int], val: int) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [3, 2, 2, 3], val = 3
Saída: 2
Lista após execução: [2, 2, _, _]
```

### Exemplo 2

```text
Entrada: nums = [1, 2, 3], val = 4
Saída: 3
Lista após execução: [1, 2, 3]
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Os valores depois da posição `k - 1` não importam.

---

## 12. Mover Zeros para o Final

**Dificuldade:** Média  
**Tópicos:** Array, dois ponteiros, in-place

### Enunciado

Dada uma lista de inteiros `nums`, mova todos os zeros para o final da lista, mantendo a ordem relativa dos elementos não zero.

A modificação deve ser feita in-place.

### Assinatura

```python
def solution(nums: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [0, 1, 0, 3, 12]
Saída: [1, 3, 12, 0, 0]
```

### Exemplo 2

```text
Entrada: nums = [0, 0, 1]
Saída: [1, 0, 0]
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

---

## 13. Segundo Maior Valor

**Dificuldade:** Média  
**Tópicos:** Array, comparação

### Enunciado

Dada uma lista de inteiros `nums`, retorne o segundo maior valor distinto presente na lista.

Se não existir segundo maior valor distinto, retorne `None`.

### Assinatura

```python
def solution(nums: list[int]) -> int | None:
    pass
```

### Exemplo 1

```text
Entrada: nums = [10, 4, 20, 8]
Saída: 10
```

### Exemplo 2

```text
Entrada: nums = [5, 5, 5]
Saída: None
```

### Exemplo 3

```text
Entrada: nums = [1, 2, 2, 3]
Saída: 2
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Observação

Tente resolver em uma única passagem.

---

## 14. Remover Duplicatas

**Dificuldade:** Média  
**Tópicos:** Array, conjunto, controle de repetição

### Enunciado

Dada uma lista de inteiros `nums`, retorne uma nova lista sem valores duplicados, preservando a primeira ocorrência de cada valor.

### Assinatura

```python
def solution(nums: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 2, 3, 1]
Saída: [1, 2, 3]
```

### Exemplo 2

```text
Entrada: nums = [4, 4, 4]
Saída: [4]
```

### Restrições

```text
0 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Variação

Resolva primeiro sem usar `set`. Depois resolva usando `set` para comparar a complexidade.

---

## 15. Remover Duplicatas de Array Ordenado

**Dificuldade:** Média  
**Tópicos:** Array, dois ponteiros, in-place

### Enunciado

Dada uma lista ordenada de inteiros `nums`, remova os valores duplicados in-place.

Retorne `k`, a quantidade de valores únicos.

Após a execução, os primeiros `k` elementos de `nums` devem conter os valores únicos em ordem.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 1, 2]
Saída: 2
Lista após execução: [1, 2, _]
```

### Exemplo 2

```text
Entrada: nums = [0, 0, 1, 1, 1, 2, 2, 3]
Saída: 4
Lista após execução: [0, 1, 2, 3, _, _, _, _]
```

### Restrições

```text
0 <= len(nums) <= 10^4
nums está ordenado em ordem não decrescente
-10^9 <= nums[i] <= 10^9
```

---

## 16. Rotacionar Array para a Direita

**Dificuldade:** Média  
**Tópicos:** Array, rotação, módulo

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `k`, retorne uma nova lista representando `nums` rotacionada `k` posições para a direita.

### Assinatura

```python
def solution(nums: list[int], k: int) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4, 5], k = 2
Saída: [4, 5, 1, 2, 3]
```

### Exemplo 2

```text
Entrada: nums = [1, 2], k = 3
Saída: [2, 1]
```

### Restrições

```text
0 <= len(nums) <= 10^4
0 <= k <= 10^9
-10^9 <= nums[i] <= 10^9
```

---

## 17. Rotacionar Array para a Direita In-Place

**Dificuldade:** Média  
**Tópicos:** Array, dois ponteiros, in-place, reversão

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `k`, rotacione a lista `k` posições para a direita in-place.

Retorne a própria lista modificada.

### Assinatura

```python
def solution(nums: list[int], k: int) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4, 5], k = 2
Saída: [4, 5, 1, 2, 3]
```

### Exemplo 2

```text
Entrada: nums = [1, 2], k = 3
Saída: [2, 1]
```

### Restrições

```text
0 <= len(nums) <= 10^4
0 <= k <= 10^9
-10^9 <= nums[i] <= 10^9
```

### Dica

Uma solução eficiente usa três reversões.

---

## 18. Mesclar Dois Arrays

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, iteração

### Enunciado

Dadas duas listas de inteiros `nums1` e `nums2`, retorne uma nova lista contendo todos os elementos de `nums1` seguidos pelos elementos de `nums2`.

### Assinatura

```python
def solution(nums1: list[int], nums2: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums1 = [1, 2], nums2 = [3, 4]
Saída: [1, 2, 3, 4]
```

### Exemplo 2

```text
Entrada: nums1 = [], nums2 = [1]
Saída: [1]
```

### Restrições

```text
0 <= len(nums1), len(nums2) <= 10^4
-10^9 <= nums1[i], nums2[i] <= 10^9
```

### Observação

Não use `+` entre listas.

---

## 19. Mesclar Arrays Ordenados

**Dificuldade:** Média  
**Tópicos:** Array, dois ponteiros, ordenação

### Enunciado

Dadas duas listas ordenadas `nums1` e `nums2`, retorne uma nova lista ordenada contendo todos os elementos das duas listas.

### Assinatura

```python
def solution(nums1: list[int], nums2: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums1 = [1, 3, 5], nums2 = [2, 4, 6]
Saída: [1, 2, 3, 4, 5, 6]
```

### Exemplo 2

```text
Entrada: nums1 = [1, 2, 10], nums2 = [3, 4]
Saída: [1, 2, 3, 4, 10]
```

### Restrições

```text
0 <= len(nums1), len(nums2) <= 10^4
nums1 e nums2 estão ordenados em ordem não decrescente
-10^9 <= nums1[i], nums2[i] <= 10^9
```

### Observação

Não use `sort()` nem `sorted()`.

---

## 20. Two Sum

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, hashmap

### Enunciado

Dada uma lista de inteiros `nums` e um inteiro `target`, retorne os índices de dois números cuja soma seja igual a `target`.

Você pode assumir que existe exatamente uma solução.

Não use o mesmo elemento duas vezes.

### Assinatura

```python
def solution(nums: list[int], target: int) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [2, 7, 11, 15], target = 9
Saída: [0, 1]
```

### Exemplo 2

```text
Entrada: nums = [3, 2, 4], target = 6
Saída: [1, 2]
```

### Restrições

```text
2 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
```

### Variação

Resolva primeiro com dois loops. Depois resolva usando dicionário.

---

## 21. Maior Soma de Dois Elementos

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, comparação

### Enunciado

Dada uma lista com pelo menos dois inteiros `nums`, retorne a maior soma possível entre dois elementos distintos da lista.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 5, 3, 9]
Saída: 14
```

### Exemplo 2

```text
Entrada: nums = [-10, -3, -5, -1]
Saída: -4
```

### Restrições

```text
2 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
```

### Dica

Você precisa encontrar os dois maiores valores.

---

## 22. Produto Exceto Ele Mesmo

**Dificuldade:** Média  
**Tópicos:** Array, prefixo, sufixo

### Enunciado

Dada uma lista de inteiros `nums`, retorne uma lista `answer` tal que `answer[i]` seja igual ao produto de todos os elementos de `nums`, exceto `nums[i]`.

Não use divisão.

### Assinatura

```python
def solution(nums: list[int]) -> list[int]:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 4]
Saída: [24, 12, 8, 6]
```

### Exemplo 2

```text
Entrada: nums = [-1, 1, 0, -3, 3]
Saída: [0, 0, 9, 0, 0]
```

### Restrições

```text
2 <= len(nums) <= 10^4
-30 <= nums[i] <= 30
```

### Dica

Pense em produto acumulado à esquerda e à direita de cada posição.

---

## 23. Melhor Momento para Comprar e Vender Ação

**Dificuldade:** Fácil/Média  
**Tópicos:** Array, mínimo acumulado, lucro máximo

### Enunciado

Dada uma lista `prices`, onde `prices[i]` representa o preço de uma ação no dia `i`, retorne o maior lucro possível comprando em um dia e vendendo em um dia posterior.

Se não for possível obter lucro, retorne `0`.

### Assinatura

```python
def solution(prices: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: prices = [7, 1, 5, 3, 6, 4]
Saída: 5
Explicação: compra no preço 1 e venda no preço 6.
```

### Exemplo 2

```text
Entrada: prices = [7, 6, 4, 3, 1]
Saída: 0
```

### Restrições

```text
1 <= len(prices) <= 10^5
0 <= prices[i] <= 10^4
```

---

## 24. Subarray de Maior Soma

**Dificuldade:** Média  
**Tópicos:** Array, Kadane, programação dinâmica simples

### Enunciado

Dada uma lista de inteiros `nums`, encontre a maior soma possível de um subarray contíguo e retorne essa soma.

### Assinatura

```python
def solution(nums: list[int]) -> int:
    pass
```

### Exemplo 1

```text
Entrada: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Saída: 6
Explicação: [4, -1, 2, 1] tem soma 6.
```

### Exemplo 2

```text
Entrada: nums = [1]
Saída: 1
```

### Restrições

```text
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
```

---

## 25. Existe Duplicata

**Dificuldade:** Fácil  
**Tópicos:** Array, set, hashmap

### Enunciado

Dada uma lista de inteiros `nums`, retorne `True` se algum valor aparecer pelo menos duas vezes. Caso contrário, retorne `False`.

### Assinatura

```python
def solution(nums: list[int]) -> bool:
    pass
```

### Exemplo 1

```text
Entrada: nums = [1, 2, 3, 1]
Saída: True
```

### Exemplo 2

```text
Entrada: nums = [1, 2, 3, 4]
Saída: False
```

### Restrições

```text
1 <= len(nums) <= 10^5
-10^9 <= nums[i] <= 10^9
```

### Variação

Resolva primeiro com dois loops. Depois resolva usando `set`.

---

# Ordem Recomendada de Estudo

```text
1. Buscar Índice de um Valor
2. Contém Valor
3. Contar Ocorrências
4. Maior Valor
5. Menor Valor
6. Soma dos Elementos
7. Média dos Elementos
8. Inverter Lista
9. Inverter Lista In-Place
10. Remover Valor
11. Remover Valor In-Place
12. Mover Zeros para o Final
13. Segundo Maior Valor
14. Remover Duplicatas
15. Remover Duplicatas de Array Ordenado
16. Rotacionar Array para a Direita
17. Rotacionar Array para a Direita In-Place
18. Mesclar Dois Arrays
19. Mesclar Arrays Ordenados
20. Two Sum
21. Maior Soma de Dois Elementos
22. Produto Exceto Ele Mesmo
23. Melhor Momento para Comprar e Vender Ação
24. Subarray de Maior Soma
25. Existe Duplicata
```

---

# Como Praticar

Para cada exercício, siga este processo:

1. Resolva primeiro da forma mais simples possível.
2. Escreva testes manuais com listas pequenas.
3. Analise a complexidade de tempo e espaço.
4. Tente melhorar a solução.
5. Refaça o exercício alguns dias depois sem olhar a resposta anterior.

Modelo de análise:

```text
Complexidade de tempo: O(?)
Complexidade de espaço: O(?)
Estratégia usada: busca linear, dois ponteiros, hashmap, prefixo/sufixo etc.
```
